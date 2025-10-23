# 15. Security and Performance

## 15.1 Security Requirements

**Frontend Security:**
- **CSP Headers:** `default-src 'self'; script-src 'self' 'unsafe-inline'; connect-src 'self' https://api.rnd-cards.example.com wss://api.rnd-cards.example.com`
- **XSS Prevention:** React auto-escaping, DOMPurify for rich text editor
- **Secure Storage:** JWT in httpOnly cookies (not localStorage for production)

**Backend Security:**
- **Input Validation:** Pydantic schemas for all API inputs, SQL injection prevention via ORM
- **Rate Limiting:** 100 requests/minute per user, 5 concurrent AI generations
- **CORS Policy:** Allow only frontend domain

**Authentication Security:**
- **Token Storage:** JWT tokens with 24-hour expiry, refresh tokens with 7-day expiry
- **Session Management:** Cognito-managed sessions
- **Password Policy:** Min 8 chars, 1 uppercase, 1 number (enforced by Cognito)

---

## 15.2 Rate Limiting Implementation

**Architecture:** Redis-based sliding window algorithm

**Implementation:**

```python
# apps/api/src/middleware/rate_limit.py
from fastapi import Request, HTTPException
from redis.asyncio import Redis
import time

class RateLimiter:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def check_rate_limit(
        self,
        user_id: str,
        limit: int = 100,
        window: int = 60  # seconds
    ) -> bool:
        """Sliding window rate limiter"""
        key = f"rate_limit:{user_id}"
        now = time.time()

        # Remove requests older than window
        await self.redis.zremrangebyscore(key, 0, now - window)

        # Count requests in current window
        current_count = await self.redis.zcard(key)

        if current_count >= limit:
            # Get oldest request timestamp
            oldest = await self.redis.zrange(key, 0, 0, withscores=True)
            if oldest:
                reset_time = int(oldest[0][1] + window)
                raise HTTPException(
                    status_code=429,
                    detail={
                        "error": "Rate limit exceeded",
                        "retryAfter": reset_time,
                        "limit": limit,
                        "window": window
                    },
                    headers={
                        "X-RateLimit-Limit": str(limit),
                        "X-RateLimit-Remaining": "0",
                        "X-RateLimit-Reset": str(reset_time),
                        "Retry-After": str(int(reset_time - now))
                    }
                )

        # Add current request
        await self.redis.zadd(key, {str(now): now})
        await self.redis.expire(key, window)

        return True

# Middleware implementation
from fastapi import Depends

async def rate_limit_middleware(
    request: Request,
    user_id: str = Depends(get_current_user)
):
    limiter = RateLimiter(request.app.state.redis)
    await limiter.check_rate_limit(user_id, limit=100, window=60)
```

**AI Generation Rate Limiting:**

```python
# apps/api/src/middleware/ai_rate_limit.py
async def ai_generation_limiter(user_id: str, redis: Redis) -> bool:
    """Limit concurrent AI generations to 5 per user"""
    key = f"ai_concurrent:{user_id}"
    current = await redis.get(key)

    if current and int(current) >= 5:
        raise HTTPException(
            status_code=429,
            detail={
                "error": "Maximum 5 concurrent AI generations exceeded",
                "message": "Poczekaj na zakończenie bieżących generacji"
            }
        )

    await redis.incr(key)
    await redis.expire(key, 3600)  # 1 hour max
    return True

# Decrement when generation completes
async def release_ai_slot(user_id: str, redis: Redis):
    key = f"ai_concurrent:{user_id}"
    await redis.decr(key)
```

**Rate Limit Headers (FastAPI Middleware):**

```python
# apps/api/src/middleware/rate_limit.py
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if hasattr(request.state, 'user_id'):
            user_id = request.state.user_id
            redis = request.app.state.redis

            # Get current usage
            key = f"rate_limit:{user_id}"
            count = await redis.zcard(key)

            response.headers["X-RateLimit-Limit"] = "100"
            response.headers["X-RateLimit-Remaining"] = str(max(0, 100 - count))
            response.headers["X-RateLimit-Reset"] = str(int(time.time() + 60))

        return response
```

---

## 15.3 Input Validation Architecture

**Pydantic Schema Examples:**

```python
# apps/api/src/schemas/batch.py
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class ProjectInputDataSchema(BaseModel):
    """Validation for Excel row data"""
    nazwaProjektu: str = Field(..., min_length=1, max_length=255)
    opis: str = Field(..., min_length=100, max_length=5000)
    dataRozpoczecia: date
    dataZakonczenia: date
    celProjektu: str = Field(..., min_length=50, max_length=2000)
    osobaOdpowiedzialna: str = Field(..., min_length=1, max_length=255)

    @validator('dataZakonczenia')
    def validate_end_date(cls, v, values):
        if 'dataRozpoczecia' in values and v < values['dataRozpoczecia']:
            raise ValueError('Data zakończenia musi być późniejsza niż data rozpoczęcia')
        return v

    @validator('nazwaProjektu', 'opis', 'celProjektu')
    def sanitize_text(cls, v):
        """Remove potentially dangerous characters"""
        # Strip HTML tags
        import re
        v = re.sub(r'<[^>]+>', '', v)
        # Remove null bytes
        v = v.replace('\x00', '')
        return v.strip()

class BatchCreateSchema(BaseModel):
    """Validation for batch creation"""
    name: str = Field(..., min_length=1, max_length=255)
    # File validation happens in route handler

    @validator('name')
    def sanitize_name(cls, v):
        import re
        # Remove special characters that could cause filesystem issues
        v = re.sub(r'[<>:"/\\|?*]', '', v)
        return v.strip()

class ProjectRegenerateSchema(BaseModel):
    """Validation for section regeneration"""
    sectionKey: str = Field(..., regex=r'^(nazwa_projektu|cel_projektu|opis_projektu|nowatorstwo|metodologia|rezultaty|koszty|harmonogram)$')
    hints: Optional[str] = Field(None, max_length=1000)
    aiModel: str = Field(default='claude', regex=r'^(claude|gpt4)$')

    @validator('hints')
    def sanitize_hints(cls, v):
        if v:
            # Remove potential prompt injection attempts
            forbidden = ['ignore previous', 'disregard', 'system:', 'assistant:']
            v_lower = v.lower()
            for phrase in forbidden:
                if phrase in v_lower:
                    raise ValueError('Niedozwolone frazy w hints')
        return v
```

**Excel Upload Validation:**

```python
# apps/api/src/services/validation_service.py
import openpyxl
from typing import List
from ..schemas.batch import ProjectInputDataSchema, ValidationError

class ExcelValidationService:
    REQUIRED_COLUMNS = [
        'Nazwa projektu',
        'Opis',
        'Data rozpoczęcia',
        'Data zakończenia',
        'Cel projektu',
        'Osoba odpowiedzialna'
    ]

    async def validate_excel(self, file_path: str) -> List[ValidationError]:
        errors = []

        try:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active

            # Validate headers
            headers = [cell.value for cell in ws[1]]
            missing_cols = set(self.REQUIRED_COLUMNS) - set(headers)
            if missing_cols:
                errors.append(ValidationError(
                    rowNumber=0,
                    columnName=', '.join(missing_cols),
                    errorType='missing_required',
                    errorMessage=f'Brakujące kolumny: {", ".join(missing_cols)}'
                ))
                return errors

            # Validate rows (max 20)
            row_count = ws.max_row - 1  # Exclude header
            if row_count > 20:
                errors.append(ValidationError(
                    rowNumber=0,
                    columnName='',
                    errorType='max_length',
                    errorMessage=f'Maksymalnie 20 projektów na plik (znaleziono {row_count})'
                ))
                return errors

            # Validate each row
            for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
                row_data = dict(zip(headers, row))

                try:
                    ProjectInputDataSchema(
                        nazwaProjektu=row_data.get('Nazwa projektu'),
                        opis=row_data.get('Opis'),
                        dataRozpoczecia=row_data.get('Data rozpoczęcia'),
                        dataZakonczenia=row_data.get('Data zakończenia'),
                        celProjektu=row_data.get('Cel projektu'),
                        osobaOdpowiedzialna=row_data.get('Osoba odpowiedzialna')
                    )
                except ValueError as e:
                    errors.append(ValidationError(
                        rowNumber=idx,
                        columnName=str(e.__cause__) if e.__cause__ else '',
                        errorType='invalid_type',
                        errorMessage=str(e)
                    ))

        except Exception as e:
            errors.append(ValidationError(
                rowNumber=0,
                columnName='',
                errorType='invalid_type',
                errorMessage=f'Nie można odczytać pliku Excel: {str(e)}'
            ))

        return errors
```

**SQL Injection Prevention (SQLAlchemy ORM):**

```python
# apps/api/src/repositories/batch_repository.py
# CORRECT - Using ORM (safe)
async def get_batches_by_status(self, user_id: str, status: str):
    result = await self.session.execute(
        select(Batch)
        .where(Batch.user_id == user_id)
        .where(Batch.status == status)  # Parameterized
    )
    return result.scalars().all()

# NEVER DO THIS - Raw SQL with string interpolation (vulnerable)
# query = f"SELECT * FROM batches WHERE user_id = '{user_id}' AND status = '{status}'"
```

---

## 15.4 Network Security Architecture

**AWS VPC Design:**

```
AWS VPC (10.0.0.0/16) - EU-Central-1
│
├── Public Subnets (10.0.1.0/24, 10.0.2.0/24)
│   ├── Application Load Balancer (ALB)
│   │   └── Security Group: sg-alb
│   │       - Inbound: 443 (0.0.0.0/0), 80 (0.0.0.0/0)
│   │       - Outbound: All to ECS security group
│   └── NAT Gateway (for private subnet internet access)
│
├── Private Subnets - App Tier (10.0.10.0/24, 10.0.11.0/24)
│   ├── ECS Fargate Tasks (API + Workers)
│   │   └── Security Group: sg-ecs-tasks
│   │       - Inbound: 8000 from ALB security group
│   │       - Outbound: 443 (AWS APIs), 5432 (RDS), 6379 (Redis)
│   │
│   └── Network ACL (Stateless firewall)
│       - Inbound: 8000, 1024-65535 (ephemeral)
│       - Outbound: All
│
└── Private Subnets - Data Tier (10.0.20.0/24, 10.0.21.0/24)
    ├── RDS PostgreSQL
    │   └── Security Group: sg-rds
    │       - Inbound: 5432 from ECS security group
    │       - Outbound: None
    │
    └── ElastiCache Redis
        └── Security Group: sg-redis
            - Inbound: 6379 from ECS security group
            - Outbound: None
```

**Security Group Rules (AWS CDK):**

```typescript
// infrastructure/lib/network-stack.ts
import * as ec2 from 'aws-cdk-lib/aws-ec2';

// ALB Security Group
const albSg = new ec2.SecurityGroup(this, 'AlbSecurityGroup', {
  vpc,
  description: 'ALB security group',
  allowAllOutbound: false
});
albSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(443), 'HTTPS from internet');
albSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'HTTP from internet (redirect to HTTPS)');

// ECS Tasks Security Group
const ecsSg = new ec2.SecurityGroup(this, 'EcsSecurityGroup', {
  vpc,
  description: 'ECS Fargate tasks security group',
  allowAllOutbound: false
});
ecsSg.addIngressRule(albSg, ec2.Port.tcp(8000), 'HTTP from ALB');
ecsSg.addEgressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(443), 'HTTPS to AWS APIs (Bedrock, S3)');
ecsSg.addEgressRule(rdsSg, ec2.Port.tcp(5432), 'PostgreSQL');
ecsSg.addEgressRule(redisSg, ec2.Port.tcp(6379), 'Redis');

// RDS Security Group
const rdsSg = new ec2.SecurityGroup(this, 'RdsSecurityGroup', {
  vpc,
  description: 'RDS PostgreSQL security group',
  allowAllOutbound: false
});
rdsSg.addIngressRule(ecsSg, ec2.Port.tcp(5432), 'PostgreSQL from ECS');

// Redis Security Group
const redisSg = new ec2.SecurityGroup(this, 'RedisSecurityGroup', {
  vpc,
  description: 'ElastiCache Redis security group',
  allowAllOutbound: false
});
redisSg.addIngressRule(ecsSg, ec2.Port.tcp(6379), 'Redis from ECS');
```

**IAM Policies (Least Privilege):**

```typescript
// infrastructure/lib/iam-stack.ts
import * as iam from 'aws-cdk-lib/aws-iam';

// ECS Task Execution Role (pulls images, writes logs)
const taskExecutionRole = new iam.Role(this, 'EcsTaskExecutionRole', {
  assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com'),
  managedPolicies: [
    iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonECSTaskExecutionRolePolicy')
  ]
});

// ECS Task Role (application permissions)
const taskRole = new iam.Role(this, 'EcsTaskRole', {
  assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com')
});

// S3 access (read/write to specific bucket only)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: [
    's3:GetObject',
    's3:PutObject',
    's3:DeleteObject'
  ],
  resources: [`arn:aws:s3:::rnd-cards-${env}/*`]
}));

// Bedrock access (specific model only)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['bedrock:InvokeModel'],
  resources: [`arn:aws:bedrock:eu-central-1::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0`]
}));

// Secrets Manager (read database credentials)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['secretsmanager:GetSecretValue'],
  resources: [`arn:aws:secretsmanager:eu-central-1:${account}:secret:rnd-cards-db-*`]
}));

// SES (send emails)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['ses:SendEmail', 'ses:SendRawEmail'],
  resources: [`arn:aws:ses:eu-central-1:${account}:identity/*`],
  conditions: {
    StringEquals: {
      'ses:FromAddress': 'noreply@rnd-cards.example.com'
    }
  }
}));
```

**WAF Configuration:**

```typescript
// infrastructure/lib/waf-stack.ts
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';

const webAcl = new wafv2.CfnWebACL(this, 'WebAcl', {
  defaultAction: { allow: {} },
  scope: 'REGIONAL',
  visibilityConfig: {
    cloudWatchMetricsEnabled: true,
    metricName: 'rnd-cards-waf',
    sampledRequestsEnabled: true
  },
  rules: [
    // AWS Managed Rules - Core Rule Set (OWASP Top 10)
    {
      name: 'AWSManagedRulesCommonRuleSet',
      priority: 1,
      statement: {
        managedRuleGroupStatement: {
          vendorName: 'AWS',
          name: 'AWSManagedRulesCommonRuleSet'
        }
      },
      overrideAction: { none: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AWSManagedRulesCommonRuleSetMetric',
        sampledRequestsEnabled: true
      }
    },
    // SQL Injection protection
    {
      name: 'AWSManagedRulesSQLiRuleSet',
      priority: 2,
      statement: {
        managedRuleGroupStatement: {
          vendorName: 'AWS',
          name: 'AWSManagedRulesSQLiRuleSet'
        }
      },
      overrideAction: { none: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AWSManagedRulesSQLiRuleSetMetric',
        sampledRequestsEnabled: true
      }
    },
    // Rate limiting (1000 requests per 5 minutes per IP)
    {
      name: 'RateLimitRule',
      priority: 3,
      statement: {
        rateBasedStatement: {
          limit: 1000,
          aggregateKeyType: 'IP'
        }
      },
      action: { block: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'RateLimitRuleMetric',
        sampledRequestsEnabled: true
      }
    }
  ]
});
```

---

## 15.5 Error Handling & Resilience Patterns

### Retry Policy Configuration

**Exponential Backoff Strategy:**

```python
# apps/api/src/services/resilience/retry_policy.py
from typing import Callable, TypeVar, Any
import asyncio
import logging

T = TypeVar('T')

class RetryConfig:
    """Retry configuration for external services"""

    # Base delays (seconds) for exponential backoff
    BASE_DELAY = 1.0
    MAX_RETRIES = 3
    MAX_TOTAL_DELAY = 30.0  # Maximum total retry time
    BACKOFF_MULTIPLIER = 4  # Delay multiplies by 4x each retry (1s, 4s, 16s)

    # Service-specific retry configurations
    RETRY_CONFIGS = {
        'bedrock': {
            'max_retries': 3,
            'base_delay': 1.0,
            'retryable_errors': ['ThrottlingException', 'ServiceUnavailableException'],
            'timeout': 180  # 3 minutes per request
        },
        'azure_openai': {
            'max_retries': 3,
            'base_delay': 2.0,
            'retryable_errors': ['RateLimitError', 'APIConnectionError'],
            'timeout': 180
        },
        'database': {
            'max_retries': 3,
            'base_delay': 0.5,
            'retryable_errors': ['OperationalError', 'TimeoutError'],
            'timeout': 10
        },
        's3': {
            'max_retries': 5,
            'base_delay': 0.5,
            'retryable_errors': ['RequestTimeout', 'ServiceUnavailable'],
            'timeout': 60
        }
    }

async def retry_with_backoff(
    func: Callable[..., T],
    service_name: str,
    *args,
    **kwargs
) -> T:
    """
    Execute function with exponential backoff retry logic.

    Args:
        func: Async function to retry
        service_name: Service identifier ('bedrock', 'azure_openai', 'database', 's3')
        *args, **kwargs: Arguments to pass to func

    Returns:
        Result from successful function execution

    Raises:
        Exception: After all retries exhausted
    """
    config = RetryConfig.RETRY_CONFIGS[service_name]
    max_retries = config['max_retries']
    base_delay = config['base_delay']
    retryable_errors = config['retryable_errors']

    logger = logging.getLogger(__name__)

    for attempt in range(max_retries):
        try:
            # Execute with timeout
            return await asyncio.wait_for(
                func(*args, **kwargs),
                timeout=config['timeout']
            )
        except asyncio.TimeoutError as e:
            logger.warning(
                f"{service_name} timeout on attempt {attempt + 1}/{max_retries}",
                extra={'service': service_name, 'attempt': attempt}
            )
            if attempt == max_retries - 1:
                raise Exception(f"Max retries exceeded for {service_name} (timeout)") from e
        except Exception as e:
            error_name = e.__class__.__name__
            is_retryable = any(err in str(e) or err == error_name for err in retryable_errors)

            if not is_retryable or attempt == max_retries - 1:
                logger.error(
                    f"{service_name} non-retryable error or max retries: {error_name}",
                    exc_info=True
                )
                raise

            # Calculate exponential backoff delay
            delay = min(
                base_delay * (RetryConfig.BACKOFF_MULTIPLIER ** attempt),
                RetryConfig.MAX_TOTAL_DELAY
            )

            logger.warning(
                f"{service_name} retryable error on attempt {attempt + 1}/{max_retries}. "
                f"Retrying in {delay}s... Error: {error_name}",
                extra={
                    'service': service_name,
                    'attempt': attempt,
                    'delay': delay,
                    'error': error_name
                }
            )

            await asyncio.sleep(delay)

    raise Exception(f"Retry logic failed for {service_name}")
```

**Usage Example:**

```python
# apps/api/src/services/ai/bedrock_service.py
from services.resilience.retry_policy import retry_with_backoff

class BedrockService:
    async def generate_card(self, prompt: str) -> str:
        """Generate project card with automatic retry"""

        async def _generate():
            response = await self.bedrock_client.invoke_model(
                modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
                body=json.dumps({
                    'anthropic_version': 'bedrock-2023-05-31',
                    'max_tokens': 4000,
                    'messages': [{'role': 'user', 'content': prompt}]
                })
            )
            return json.loads(response['body'].read())['content'][0]['text']

        # Automatically retries with exponential backoff (1s, 4s, 16s)
        return await retry_with_backoff(_generate, 'bedrock')
```

---

### Circuit Breaker Implementation

**Circuit Breaker Pattern:**

```python
# apps/api/src/services/resilience/circuit_breaker.py
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, TypeVar
import asyncio
import logging

T = TypeVar('T')

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, reject requests immediately
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    """
    Circuit breaker for AI services to prevent cascading failures.

    States:
    - CLOSED: Normal operation, requests pass through
    - OPEN: Too many failures, reject requests immediately (return fallback)
    - HALF_OPEN: After reset timeout, allow 1 test request

    Configuration:
    - Failure threshold: 3 consecutive failures → OPEN
    - Reset timeout: 60 seconds in OPEN before → HALF_OPEN
    - Success threshold in HALF_OPEN: 1 success → CLOSED
    """

    def __init__(
        self,
        service_name: str,
        failure_threshold: int = 3,
        reset_timeout: int = 60,  # seconds
        success_threshold: int = 1
    ):
        self.service_name = service_name
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: datetime | None = None

        self.logger = logging.getLogger(__name__)

    async def call(
        self,
        func: Callable[..., T],
        fallback: Callable[..., T] | None = None,
        *args,
        **kwargs
    ) -> T:
        """
        Execute function with circuit breaker protection.

        Args:
            func: Function to execute
            fallback: Optional fallback function when circuit is OPEN
            *args, **kwargs: Arguments for func

        Returns:
            Result from func or fallback

        Raises:
            Exception: If circuit is OPEN and no fallback provided
        """
        # Check if we should transition from OPEN → HALF_OPEN
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.logger.info(
                    f"Circuit breaker for {self.service_name}: OPEN → HALF_OPEN (testing recovery)"
                )
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
            else:
                # Circuit still open, use fallback
                self.logger.warning(
                    f"Circuit breaker for {self.service_name} is OPEN. Using fallback."
                )
                if fallback:
                    return await fallback(*args, **kwargs)
                else:
                    raise Exception(
                        f"Service {self.service_name} is unavailable (circuit breaker OPEN)"
                    )

        # Attempt the call
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()

            # If circuit just opened, use fallback
            if self.state == CircuitState.OPEN and fallback:
                self.logger.warning(
                    f"Circuit breaker OPENED for {self.service_name}. Using fallback."
                )
                return await fallback(*args, **kwargs)

            raise

    def _on_success(self):
        """Handle successful call"""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.logger.info(
                    f"Circuit breaker for {self.service_name}: HALF_OPEN → CLOSED (service recovered)"
                )
                self.state = CircuitState.CLOSED
                self.failure_count = 0
        elif self.state == CircuitState.CLOSED:
            # Reset failure count on success
            self.failure_count = 0

    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()

        if self.state == CircuitState.HALF_OPEN:
            # Failure during test → back to OPEN
            self.logger.warning(
                f"Circuit breaker for {self.service_name}: HALF_OPEN → OPEN (test failed)"
            )
            self.state = CircuitState.OPEN
        elif self.state == CircuitState.CLOSED:
            if self.failure_count >= self.failure_threshold:
                self.logger.error(
                    f"Circuit breaker for {self.service_name}: CLOSED → OPEN "
                    f"({self.failure_count} consecutive failures)"
                )
                self.state = CircuitState.OPEN

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset"""
        if self.last_failure_time is None:
            return False

        elapsed = (datetime.now() - self.last_failure_time).total_seconds()
        return elapsed >= self.reset_timeout

# Global circuit breakers for AI services
bedrock_breaker = CircuitBreaker('bedrock', failure_threshold=3, reset_timeout=60)
azure_openai_breaker = CircuitBreaker('azure_openai', failure_threshold=3, reset_timeout=60)
```

**Usage with Fallback:**

```python
# apps/api/src/services/ai/ai_orchestrator.py
from services.resilience.circuit_breaker import bedrock_breaker, azure_openai_breaker

class AIOrchestrator:
    """Orchestrates AI generation with circuit breaker and failover"""

    async def generate_with_failover(self, prompt: str, project_data: dict) -> str:
        """
        Generate card with primary (Bedrock) and fallback (Azure OpenAI).
        Circuit breaker prevents cascading failures.
        """

        # Try Bedrock (primary) with circuit breaker
        try:
            async def _bedrock_call():
                return await self.bedrock_service.generate_card(prompt)

            async def _azure_fallback():
                self.logger.info("Using Azure OpenAI fallback (Bedrock circuit OPEN)")
                return await self.azure_service.generate_card(prompt)

            result = await bedrock_breaker.call(
                _bedrock_call,
                fallback=_azure_fallback
            )

            return result

        except Exception as e:
            # Both services failed, return degraded response
            self.logger.error(f"All AI services failed: {e}", exc_info=True)
            return self._generate_degraded_response(project_data)

    def _generate_degraded_response(self, project_data: dict) -> str:
        """
        Generate basic template when AI unavailable.
        Allows consultant to save draft and retry later.
        """
        return f"""
# {project_data['nazwaProjektu']}

**Status:** Wersja robocza - AI tymczasowo niedostępne

# Opis projektu
{project_data['opis']}

# Cel projektu
{project_data['celProjektu']}

# Harmonogram
- Data rozpoczęcia: {project_data['dataRozpoczecia']}
- Data zakończenia: {project_data['dataZakonczenia']}

---
*Ta karta wymaga uzupełnienia. AI jest tymczasowo niedostępne. Możesz zapisać jako wersję roboczą i wygenerować ponownie później.*
"""
```

---

### Timeout Handling

**Global Timeout Middleware:**

```python
# apps/api/src/middleware/timeout_middleware.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio
import logging

class TimeoutMiddleware(BaseHTTPMiddleware):
    """
    Global timeout middleware for API requests.

    Timeouts:
    - AI generation endpoints: 15 minutes (900s)
    - Standard API endpoints: 30 seconds
    - Health checks: 5 seconds
    """

    TIMEOUT_CONFIG = {
        '/api/batches/generate': 900,  # 15 minutes for AI generation
        '/api/projects/regenerate': 900,
        '/api/batches': 30,
        '/api/projects': 30,
        '/health': 5,
        'default': 30
    }

    async def dispatch(self, request: Request, call_next):
        # Determine timeout based on path
        timeout = self._get_timeout(request.url.path)

        logger = logging.getLogger(__name__)
        logger.debug(f"Request to {request.url.path} with {timeout}s timeout")

        try:
            response = await asyncio.wait_for(
                call_next(request),
                timeout=timeout
            )
            return response

        except asyncio.TimeoutError:
            logger.error(
                f"Request timeout after {timeout}s: {request.method} {request.url.path}",
                extra={
                    'method': request.method,
                    'path': request.url.path,
                    'timeout': timeout
                }
            )

            # Return 504 Gateway Timeout with Polish message
            raise HTTPException(
                status_code=504,
                detail={
                    'error': 'timeout',
                    'message': f'Żądanie przekroczyło limit czasu ({timeout}s). Spróbuj ponownie później.',
                    'timeout_seconds': timeout
                }
            )

    def _get_timeout(self, path: str) -> int:
        """Get timeout for specific path"""
        for pattern, timeout in self.TIMEOUT_CONFIG.items():
            if pattern in path:
                return timeout
        return self.TIMEOUT_CONFIG['default']
```

**Celery Task Timeouts:**

```python
# apps/worker/src/tasks/ai_generation.py
from celery import Task
from celery.exceptions import SoftTimeLimitExceeded

@celery_app.task(
    bind=True,
    soft_time_limit=900,  # 15 minutes soft limit (allows cleanup)
    time_limit=960,  # 16 minutes hard limit (force kill)
    max_retries=1,
    retry_backoff=True
)
def generate_project_card_task(self, project_id: str, prompt: str) -> dict:
    """
    Generate project card with timeout protection.

    Soft limit (900s): Raises SoftTimeLimitExceeded, allows cleanup
    Hard limit (960s): Force kills task
    """
    try:
        # Generate card
        result = ai_orchestrator.generate_with_failover(prompt, project_data)

        return {
            'status': 'success',
            'content': result,
            'project_id': project_id
        }

    except SoftTimeLimitExceeded:
        logger.warning(f"Task soft timeout for project {project_id}")

        # Mark project as failed in database
        project_repo.update_status(project_id, 'generation_timeout')

        return {
            'status': 'timeout',
            'message': 'Generowanie przekroczyło limit 15 minut',
            'project_id': project_id
        }

    except Exception as e:
        logger.error(f"Task failed for project {project_id}: {e}", exc_info=True)
        raise self.retry(exc=e, countdown=60)  # Retry after 60s
```

---

### Degraded Mode Strategy

**Service Availability Matrix:**

| Component | Status | Available Features | Unavailable Features |
|-----------|--------|-------------------|---------------------|
| **AI Services DOWN** | Degraded | - Upload Excel<br>- View past batches<br>- Edit saved projects<br>- Export saved projects<br>- Save drafts | - AI generation<br>- Quality scoring<br>- Auto-validation |
| **Database DOWN** | Critical | - None (system offline) | - All features |
| **S3 DOWN** | Degraded | - AI generation (with temp storage)<br>- View metadata<br>- Edit projects | - Excel uploads<br>- Word exports<br>- File downloads |
| **Redis DOWN** | Degraded | - All core features (slower)<br>- Auth via Cognito directly | - Real-time status updates<br>- Rate limiting<br>- Session caching |

**Degraded Mode Implementation:**

```python
# apps/api/src/services/degraded_mode.py
from enum import Enum

class ServiceHealth(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

class DegradedModeService:
    """Manages system behavior during service outages"""

    def __init__(self):
        self.service_health = {
            'bedrock': ServiceHealth.HEALTHY,
            'azure_openai': ServiceHealth.HEALTHY,
            'database': ServiceHealth.HEALTHY,
            's3': ServiceHealth.HEALTHY,
            'redis': ServiceHealth.HEALTHY
        }

    def get_system_status(self) -> dict:
        """Return overall system health"""
        critical_services = ['database']
        degraded_services = [
            name for name, health in self.service_health.items()
            if health == ServiceHealth.DEGRADED
        ]
        unavailable_services = [
            name for name, health in self.service_health.items()
            if health == ServiceHealth.UNAVAILABLE
        ]

        # System is CRITICAL if database is down
        if 'database' in unavailable_services:
            return {
                'status': 'critical',
                'message': 'System tymczasowo niedostępny',
                'available_features': []
            }

        # System is DEGRADED if AI or storage unavailable
        if unavailable_services or degraded_services:
            available_features = self._get_available_features(unavailable_services)
            return {
                'status': 'degraded',
                'message': 'Niektóre funkcje mogą być niedostępne',
                'available_features': available_features,
                'unavailable_services': unavailable_services + degraded_services
            }

        return {
            'status': 'healthy',
            'message': 'System działa prawidłowo',
            'available_features': ['all']
        }

    def _get_available_features(self, unavailable_services: list) -> list:
        """Determine which features work with current service availability"""
        all_features = [
            'excel_upload', 'ai_generation', 'edit_projects',
            'export_word', 'view_batches', 'quality_scoring'
        ]

        # Remove features based on unavailable services
        available = all_features.copy()

        if 'bedrock' in unavailable_services and 'azure_openai' in unavailable_services:
            available.remove('ai_generation')
            available.remove('quality_scoring')

        if 's3' in unavailable_services:
            available.remove('excel_upload')
            available.remove('export_word')

        return available

# Endpoint to expose health status
@router.get('/health/detailed')
async def get_detailed_health(
    degraded_service: DegradedModeService = Depends()
) -> dict:
    """
    Returns detailed system health status.
    Frontend uses this to show degraded mode warnings.
    """
    return degraded_service.get_system_status()
```

**Frontend Degraded Mode UI:**

```typescript
// apps/web/src/components/DegradedModeWarning.tsx
import { Alert, AlertTitle } from '@mui/material';
import { useQuery } from '@tanstack/react-query';

export function DegradedModeWarning() {
  const { data: health } = useQuery({
    queryKey: ['health'],
    queryFn: () => api.get('/health/detailed'),
    refetchInterval: 30000  // Check every 30s
  });

  if (!health || health.status === 'healthy') {
    return null;
  }

  if (health.status === 'critical') {
    return (
      <Alert severity="error">
        <AlertTitle>System tymczasowo niedostępny</AlertTitle>
        {health.message}. Spróbuj ponownie za kilka minut.
      </Alert>
    );
  }

  // Degraded mode
  return (
    <Alert severity="warning">
      <AlertTitle>Tryb ograniczony</AlertTitle>
      {health.message}. Funkcje AI mogą być tymczasowo niedostępne.
      Możesz kontynuować pracę z zapisanymi projektami.
    </Alert>
  );
}
```

---

## 15.6 Deployment & Rollback Procedures

### Blue-Green Deployment Strategy

**Deployment Architecture:**

```
Production Traffic Flow:

┌─────────────┐
│   Route 53  │  (DNS: rnd-cards.example.com)
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────────┐
│  Application Load Balancer (ALB)         │
│  - Target Group: Blue (100% traffic)     │
│  - Target Group: Green (0% traffic)      │
└────┬─────────────────────────────┬───────┘
     │                             │
     ▼                             ▼
┌─────────────┐              ┌─────────────┐
│  ECS Service│              │  ECS Service│
│  (Blue)     │              │  (Green)    │
│  Version    │              │  Version    │
│  v1.2.3     │              │  v1.2.4     │
└─────────────┘              └─────────────┘
 ACTIVE                       STANDBY
```

**Deployment Steps:**

```yaml
# .github/workflows/deploy-production.yml
name: Deploy to Production (Blue-Green)

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to deploy (e.g., v1.2.4)'
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # 1. Build and push Docker images
      - name: Build Docker images
        run: |
          docker build -t rnd-cards-api:${{ inputs.version }} -f apps/api/Dockerfile .
          docker build -t rnd-cards-web:${{ inputs.version }} -f apps/web/Dockerfile .
          docker push rnd-cards-api:${{ inputs.version }}
          docker push rnd-cards-web:${{ inputs.version }}

      # 2. Run database migrations (safe, backward-compatible only)
      - name: Run database migrations
        run: |
          # Migrations must be backward-compatible with current version
          alembic upgrade head

      # 3. Deploy to GREEN environment (standby)
      - name: Deploy to Green (standby)
        run: |
          aws ecs update-service \
            --cluster rnd-cards-prod \
            --service rnd-cards-green \
            --task-definition rnd-cards:${{ inputs.version }} \
            --force-new-deployment

          # Wait for GREEN to be healthy
          aws ecs wait services-stable \
            --cluster rnd-cards-prod \
            --services rnd-cards-green

      # 4. Run smoke tests against GREEN
      - name: Smoke tests (Green environment)
        run: |
          npm run test:smoke -- --base-url https://green.rnd-cards-internal.example.com

      # 5. Switch traffic: Blue (100%) → Green (10%)
      - name: Gradual traffic shift (10%)
        run: |
          aws elbv2 modify-listener \
            --listener-arn $ALB_LISTENER_ARN \
            --default-actions \
              Type=forward,ForwardConfig='{
                "TargetGroups": [
                  {"TargetGroupArn": "$GREEN_TG_ARN", "Weight": 10},
                  {"TargetGroupArn": "$BLUE_TG_ARN", "Weight": 90}
                ]
              }'

          # Monitor for 5 minutes
          sleep 300

      # 6. Check metrics (error rate, latency)
      - name: Validate metrics
        run: |
          python scripts/check_deployment_metrics.py \
            --threshold-error-rate 1.0 \
            --threshold-p99-latency 2000

      # 7. Switch traffic: Blue (0%) → Green (100%)
      - name: Complete traffic shift (100%)
        run: |
          aws elbv2 modify-listener \
            --listener-arn $ALB_LISTENER_ARN \
            --default-actions \
              Type=forward,ForwardConfig='{
                "TargetGroups": [
                  {"TargetGroupArn": "$GREEN_TG_ARN", "Weight": 100}
                ]
              }'

      # 8. Monitor for 10 minutes
      - name: Final monitoring
        run: |
          sleep 600
          python scripts/check_deployment_metrics.py

      # 9. Mark BLUE as standby (keep running for fast rollback)
      - name: Success - Keep Blue as standby
        run: |
          echo "Deployment successful. Blue environment remains as standby for 24h."
          # Blue will be terminated after 24h if no rollback needed
```

---

### Rollback Procedures

**Automated Rollback Triggers:**

```python
# scripts/check_deployment_metrics.py
import boto3
import sys
from datetime import datetime, timedelta

class DeploymentValidator:
    """
    Validates deployment health and triggers rollback if needed.

    Rollback triggers:
    - Error rate > 1% (from <0.1% baseline)
    - P99 latency > 2000ms (from ~500ms baseline)
    - 5xx errors > 10 in 5 minutes
    - Health check failures > 3 consecutive
    """

    THRESHOLDS = {
        'error_rate_percent': 1.0,
        'p99_latency_ms': 2000,
        'error_5xx_count': 10,
        'failed_health_checks': 3
    }

    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.ecs = boto3.client('ecs')
        self.elb = boto3.client('elbv2')

    def validate_deployment(self) -> bool:
        """
        Check all metrics. Return False if rollback needed.
        """
        metrics_ok = True

        # 1. Check error rate
        error_rate = self._get_error_rate()
        if error_rate > self.THRESHOLDS['error_rate_percent']:
            print(f"❌ Error rate {error_rate}% exceeds threshold {self.THRESHOLDS['error_rate_percent']}%")
            metrics_ok = False
        else:
            print(f"✅ Error rate: {error_rate}%")

        # 2. Check P99 latency
        p99_latency = self._get_p99_latency()
        if p99_latency > self.THRESHOLDS['p99_latency_ms']:
            print(f"❌ P99 latency {p99_latency}ms exceeds threshold {self.THRESHOLDS['p99_latency_ms']}ms")
            metrics_ok = False
        else:
            print(f"✅ P99 latency: {p99_latency}ms")

        # 3. Check 5xx errors
        error_5xx_count = self._get_5xx_count()
        if error_5xx_count > self.THRESHOLDS['error_5xx_count']:
            print(f"❌ 5xx errors {error_5xx_count} exceeds threshold {self.THRESHOLDS['error_5xx_count']}")
            metrics_ok = False
        else:
            print(f"✅ 5xx errors: {error_5xx_count}")

        # 4. Check health checks
        failed_health_checks = self._get_failed_health_checks()
        if failed_health_checks > self.THRESHOLDS['failed_health_checks']:
            print(f"❌ Failed health checks {failed_health_checks} exceeds threshold {self.THRESHOLDS['failed_health_checks']}")
            metrics_ok = False
        else:
            print(f"✅ Failed health checks: {failed_health_checks}")

        return metrics_ok

    def _get_error_rate(self) -> float:
        """Calculate error rate from CloudWatch"""
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=5)

        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='HTTPCode_Target_5XX_Count',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )

        error_count = response['Datapoints'][0]['Sum'] if response['Datapoints'] else 0

        # Get total request count
        response_total = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='RequestCount',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )

        total_count = response_total['Datapoints'][0]['Sum'] if response_total['Datapoints'] else 1

        return (error_count / total_count) * 100 if total_count > 0 else 0.0

    def _get_p99_latency(self) -> float:
        """Get P99 latency from CloudWatch"""
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=5)

        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='TargetResponseTime',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            ExtendedStatistics=['p99']
        )

        return response['Datapoints'][0]['ExtendedStatistics']['p99'] * 1000 if response['Datapoints'] else 0.0

    # ... (similar methods for 5xx count and health checks)

if __name__ == '__main__':
    validator = DeploymentValidator()

    if not validator.validate_deployment():
        print("\n🚨 DEPLOYMENT VALIDATION FAILED - INITIATING ROLLBACK")
        sys.exit(1)  # Non-zero exit triggers rollback in CI/CD

    print("\n✅ Deployment validation passed")
    sys.exit(0)
```

**Manual Rollback Procedure:**

```bash
#!/bin/bash
# scripts/rollback.sh - Manual rollback to previous version

set -e

CLUSTER="rnd-cards-prod"
BLUE_SERVICE="rnd-cards-blue"
GREEN_SERVICE="rnd-cards-green"
ALB_LISTENER_ARN="arn:aws:elasticloadbalancing:..."
BLUE_TG_ARN="arn:aws:elasticloadbalancing:..."
GREEN_TG_ARN="arn:aws:elasticloadbalancing:..."

echo "🔄 Starting rollback procedure..."

# 1. Immediately switch traffic back to BLUE (previous version)
echo "Step 1: Switching 100% traffic to Blue (previous version)"
aws elbv2 modify-listener \
  --listener-arn $ALB_LISTENER_ARN \
  --default-actions \
    Type=forward,ForwardConfig="{
      \"TargetGroups\": [
        {\"TargetGroupArn\": \"$BLUE_TG_ARN\", \"Weight\": 100}
      ]
    }"

echo "✅ Traffic switched to Blue"

# 2. Verify Blue is healthy
echo "Step 2: Verifying Blue environment health"
aws elbv2 describe-target-health \
  --target-group-arn $BLUE_TG_ARN

# 3. Stop Green service
echo "Step 3: Scaling down Green service"
aws ecs update-service \
  --cluster $CLUSTER \
  --service $GREEN_SERVICE \
  --desired-count 0

echo "✅ Rollback complete. Blue (previous version) is now serving 100% traffic."
echo "📊 Monitor metrics: https://console.aws.amazon.com/cloudwatch/..."
```

**Rollback Decision Matrix:**

| Metric | Threshold | Action | Severity |
|--------|-----------|--------|----------|
| Error rate > 1% | 5 minutes sustained | **Automatic rollback** | Critical |
| P99 latency > 2000ms | 5 minutes sustained | **Automatic rollback** | Critical |
| 5xx errors > 10 | In 5-minute window | **Automatic rollback** | Critical |
| Health checks failing | 3 consecutive | **Automatic rollback** | Critical |
| User reports | >5 critical bugs | **Manual rollback** | High |
| Database migration error | Any failure | **Manual rollback + DB rollback** | Critical |

---

### Database Migration Safety

**Backward-Compatible Migration Guidelines:**

```python
# apps/api/migrations/versions/20250122_add_quality_metrics.py
"""
Add quality metrics columns to projects table.

IMPORTANT: This migration is backward-compatible.
- Columns added with DEFAULT values (no data loss)
- Old code (Blue) can still run during deployment
- New code (Green) uses new columns

Revision ID: a1b2c3d4e5f6
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    """
    Add quality metrics columns (backward-compatible).
    Blue environment (old code) ignores these columns.
    """
    # Add columns with DEFAULT to avoid breaking old code
    op.add_column('projects',
        sa.Column('quality_score', sa.Integer(), nullable=True, server_default='0')
    )
    op.add_column('projects',
        sa.Column('validation_errors', sa.JSON(), nullable=True, server_default='[]')
    )

    # Backfill existing rows (optional, can be done in background)
    # op.execute("UPDATE projects SET quality_score = 0 WHERE quality_score IS NULL")

def downgrade():
    """
    Rollback: Remove quality metrics columns.
    Only run this if rollback is needed within 24h of deployment.
    """
    op.drop_column('projects', 'quality_score')
    op.drop_column('projects', 'validation_errors')
```

**Migration Rollback Procedure:**

```bash
#!/bin/bash
# scripts/rollback-migration.sh

set -e

echo "🔄 Rolling back database migration..."

# 1. Identify current migration version
CURRENT_VERSION=$(alembic current)
echo "Current version: $CURRENT_VERSION"

# 2. Rollback to previous version
PREVIOUS_VERSION="$1"  # Pass as argument

if [ -z "$PREVIOUS_VERSION" ]; then
  echo "❌ Error: Must specify previous version"
  echo "Usage: ./rollback-migration.sh <previous_version_id>"
  exit 1
fi

# 3. Confirm rollback
echo "⚠️  WARNING: Rolling back from $CURRENT_VERSION to $PREVIOUS_VERSION"
read -p "Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
  echo "Rollback cancelled"
  exit 0
fi

# 4. Execute rollback
echo "Rolling back migration..."
alembic downgrade $PREVIOUS_VERSION

echo "✅ Migration rollback complete"
echo "📊 Verify database state manually"
```

**Migration Safety Checklist:**

- [ ] Migration is backward-compatible (Blue can run with new schema)
- [ ] No columns dropped (use deprecation instead)
- [ ] No NOT NULL columns without DEFAULT
- [ ] Tested rollback procedure in staging
- [ ] Database backup taken before migration
- [ ] Monitoring alerts configured for migration errors

---

### Smoke Test Definitions

**Critical User Paths (5 tests):**

```typescript
// apps/api/tests/smoke/smoke-tests.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Smoke tests run after deployment to validate critical paths.
 * Must complete in <2 minutes total.
 */

test.describe('Smoke Tests - Critical Paths', () => {

  // 1. Authentication flow
  test('Path 1: User can authenticate', async ({ page }) => {
    await page.goto('/login');

    await page.fill('input[name="email"]', 'smoke-test@example.com');
    await page.fill('input[name="password"]', process.env.SMOKE_TEST_PASSWORD);
    await page.click('button[type="submit"]');

    // Should redirect to dashboard
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('text=Witaj')).toBeVisible();
  });

  // 2. Excel upload + batch creation
  test('Path 2: User can upload Excel and create batch', async ({ page }) => {
    await page.goto('/dashboard');

    // Upload Excel file
    await page.setInputFiles('input[type="file"]', 'tests/fixtures/test-batch-5-projects.xlsx');
    await page.fill('input[name="batchName"]', `Smoke Test ${Date.now()}`);
    await page.click('button:has-text("Prześlij")');

    // Should see batch in list
    await expect(page.locator('text=Smoke Test')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('text=5 projektów')).toBeVisible();
  });

  // 3. AI generation (single project)
  test('Path 3: User can generate project card with AI', async ({ page }) => {
    await page.goto('/dashboard');

    // Find test batch (created by previous test or setup)
    await page.click('text=Smoke Test Batch');

    // Click generate for first project
    await page.click('button:has-text("Generuj"):first');

    // Wait for generation (max 180s)
    await expect(page.locator('text=Generowanie zakończone')).toBeVisible({ timeout: 180000 });

    // Verify content exists
    const content = await page.locator('.project-card-content').textContent();
    expect(content.length).toBeGreaterThan(500);  // Should have substantial content
  });

  // 4. Project review + edit
  test('Path 4: User can review and edit generated card', async ({ page }) => {
    await page.goto('/dashboard');

    await page.click('text=Smoke Test Batch');
    await page.click('button:has-text("Przejrzyj"):first');

    // Should see editor
    await expect(page.locator('.project-editor')).toBeVisible();

    // Make an edit
    await page.fill('textarea[name="opis"]', 'Edytowany opis projektu (smoke test)');
    await page.click('button:has-text("Zapisz")');

    // Should see success message
    await expect(page.locator('text=Zapisano zmiany')).toBeVisible();
  });

  // 5. Word export
  test('Path 5: User can export batch to Word', async ({ page }) => {
    await page.goto('/dashboard');

    await page.click('text=Smoke Test Batch');

    // Start download
    const downloadPromise = page.waitForEvent('download');
    await page.click('button:has-text("Eksportuj do Word")');
    const download = await downloadPromise;

    // Verify download
    expect(download.suggestedFilename()).toContain('Smoke_Test');
    expect(download.suggestedFilename()).toContain('.docx');

    // Verify file size (should be >50KB for 5 projects)
    const path = await download.path();
    const fs = require('fs');
    const stats = fs.statSync(path);
    expect(stats.size).toBeGreaterThan(50000);
  });
});

/**
 * API Health Checks
 */
test.describe('Smoke Tests - API Health', () => {

  test('API /health returns 200', async ({ request }) => {
    const response = await request.get('/api/health');
    expect(response.status()).toBe(200);

    const body = await response.json();
    expect(body.status).toBe('healthy');
  });

  test('API /health/detailed shows all services healthy', async ({ request }) => {
    const response = await request.get('/api/health/detailed');
    expect(response.status()).toBe(200);

    const body = await response.json();
    expect(body.database).toBe('healthy');
    expect(body.redis).toBe('healthy');
    expect(body.s3).toBe('healthy');
  });
});
```

**Running Smoke Tests:**

```bash
# Run smoke tests against specific environment
npm run test:smoke -- --base-url https://green.rnd-cards-internal.example.com

# Expected output:
# ✅ Path 1: User can authenticate (2.1s)
# ✅ Path 2: User can upload Excel and create batch (5.3s)
# ✅ Path 3: User can generate project card with AI (45.2s)
# ✅ Path 4: User can review and edit generated card (3.8s)
# ✅ Path 5: User can export batch to Word (4.1s)
# ✅ API /health returns 200 (0.2s)
# ✅ API /health/detailed shows all services healthy (0.3s)
#
# Total: 7 passed (60.0s)
```

---

## 15.2 Performance Optimization

**Frontend Performance:**
- **Bundle Size Target:** <500KB initial JS (gzipped)
- **Loading Strategy:** Code splitting by route, lazy loading components
- **Caching Strategy:** React Query with 5-minute stale time for batches, 1-minute for projects

**Backend Performance:**
- **Response Time Target:** <200ms for API endpoints (except AI generation)
- **Database Optimization:** Indexed queries, connection pooling (max 20 connections)
- **Caching Strategy:** Redis cache for user sessions (24-hour TTL), batch metadata (5-minute TTL)

---
