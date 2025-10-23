# 7. External APIs

## AWS Bedrock (Claude 3.5 Sonnet)

- **Purpose:** Primary AI engine for Polish project card generation
- **Documentation:** https://docs.aws.amazon.com/bedrock/
- **Base URL:** `bedrock-runtime.eu-central-1.amazonaws.com`
- **Authentication:** AWS IAM credentials (via boto3)
- **Rate Limits:** 5 concurrent requests (application-enforced)

**Key Endpoints:**
- `POST /model/anthropic.claude-3-5-sonnet-20241022-v2:0/invoke` - Generate text

**Integration Notes:**
- Use boto3 SDK with exponential backoff retry
- Context window: 200K tokens
- Temperature: 0.5 for balanced creativity/consistency
- Cost: ~€0.10-0.14 per project card

---

## Azure OpenAI Service (GPT-4)

- **Purpose:** Failover AI engine when Bedrock unavailable
- **Documentation:** https://learn.microsoft.com/azure/ai-services/openai/
- **Base URL:** `https://westeurope.api.cognitive.microsoft.com/openai/deployments/`
- **Authentication:** API key
- **Rate Limits:** 10 requests/minute

**Key Endpoints:**
- `POST /{deployment-id}/chat/completions` - Generate chat completion

**Integration Notes:**
- Only used when Bedrock fails 3 consecutive times (circuit breaker)
- Automatic fallback, transparent to user
- Cost: ~€0.12-0.16 per project card (slightly higher than Claude)

---

## LanguageTool API

- **Purpose:** Polish grammar checking for quality scoring
- **Documentation:** https://languagetool.org/http-api/
- **Base URL:** `https://api.languagetool.org/v2/`
- **Authentication:** API key (or self-hosted)
- **Rate Limits:** 20 requests/minute (free tier)

**Key Endpoints:**
- `POST /check` - Check text for grammar/style errors

**Integration Notes:**
- Language: `pl-PL`
- Used asynchronously during quality scoring
- Consider self-hosted instance for production (no rate limits)

---

## Amazon SES

- **Purpose:** Transactional emails (password reset, notifications)
- **Documentation:** https://docs.aws.amazon.com/ses/
- **Authentication:** AWS IAM
- **Rate Limits:** 14 emails/second (verified account)

**Key Operations:**
- Send password reset emails
- Send batch completion notifications (optional future feature)

**Integration Notes:**
- Requires email verification for sender address
- Use templates for consistent branding

---
