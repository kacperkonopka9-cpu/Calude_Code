# 9. Database Schema

PostgreSQL 15+ with JSONB for semi-structured data.

## SQL Schema (DDL)

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    cognito_sub VARCHAR(255) UNIQUE NOT NULL, -- AWS Cognito user ID
    preferences JSONB NOT NULL DEFAULT '{"defaultAiModel": "claude", "language": "pl", "notificationsEnabled": true}',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_cognito_sub ON users(cognito_sub);

-- Batches table
CREATE TABLE batches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'uploading',
    total_projects INTEGER NOT NULL CHECK (total_projects BETWEEN 1 AND 20),
    completed_projects INTEGER NOT NULL DEFAULT 0,
    average_quality_score DECIMAL(5,2) DEFAULT 0 CHECK (average_quality_score BETWEEN 0 AND 100),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL, -- created_at + 90 days
    CONSTRAINT valid_status CHECK (status IN ('uploading', 'validating', 'validation_failed', 'queued', 'processing', 'completed', 'partially_completed', 'archived'))
);

CREATE INDEX idx_batches_user_id ON batches(user_id);
CREATE INDEX idx_batches_status ON batches(status);
CREATE INDEX idx_batches_created_at ON batches(created_at DESC);
CREATE INDEX idx_batches_expires_at ON batches(expires_at);

-- Projects table
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    batch_id UUID NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL CHECK (row_number BETWEEN 1 AND 20),
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    quality_score DECIMAL(5,2) DEFAULT 0 CHECK (quality_score BETWEEN 0 AND 100),
    input_data JSONB NOT NULL, -- ProjectInputData
    ai_model VARCHAR(50) DEFAULT 'claude-3.5-sonnet',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    generated_at TIMESTAMP WITH TIME ZONE,
    edited_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT valid_project_status CHECK (status IN ('pending', 'generating', 'completed', 'failed', 'reviewed', 'exported')),
    UNIQUE(batch_id, row_number)
);

CREATE INDEX idx_projects_batch_id ON projects(batch_id);
CREATE INDEX idx_projects_status ON projects(status);

-- Project content table (1:1 with projects)
CREATE TABLE project_contents (
    project_id UUID PRIMARY KEY REFERENCES projects(id) ON DELETE CASCADE,
    sections JSONB NOT NULL, -- Record<SectionKey, SectionContent>
    version INTEGER NOT NULL DEFAULT 1,
    last_edited_section VARCHAR(50)
);

-- Generation metadata table (1:1 with projects)
CREATE TABLE generation_metadata (
    project_id UUID PRIMARY KEY REFERENCES projects(id) ON DELETE CASCADE,
    attempts INTEGER NOT NULL DEFAULT 1 CHECK (attempts BETWEEN 1 AND 3),
    total_input_tokens INTEGER NOT NULL DEFAULT 0,
    total_output_tokens INTEGER NOT NULL DEFAULT 0,
    total_cost_eur DECIMAL(10,4) NOT NULL DEFAULT 0,
    average_latency_ms INTEGER,
    model_used VARCHAR(50) NOT NULL,
    errors JSONB DEFAULT '[]', -- Array of ApiError
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Validation errors table
CREATE TABLE validation_errors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    batch_id UUID NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL,
    column_name VARCHAR(100) NOT NULL,
    error_type VARCHAR(50) NOT NULL,
    error_message TEXT NOT NULL,
    CONSTRAINT valid_error_type CHECK (error_type IN ('missing_required', 'invalid_type', 'min_length', 'max_length', 'invalid_date', 'date_logic_error'))
);

CREATE INDEX idx_validation_errors_batch_id ON validation_errors(batch_id);

-- Export history table
CREATE TABLE export_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    s3_key VARCHAR(500) NOT NULL,
    file_size_bytes INTEGER NOT NULL,
    exported_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL -- exported_at + 30 days
);

CREATE INDEX idx_export_history_project_id ON export_history(project_id);
CREATE INDEX idx_export_history_user_id ON export_history(user_id);
CREATE INDEX idx_export_history_expires_at ON export_history(expires_at);

-- Trigger to update batch average quality score
CREATE OR REPLACE FUNCTION update_batch_quality_score()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE batches
    SET average_quality_score = (
        SELECT AVG(quality_score)
        FROM projects
        WHERE batch_id = NEW.batch_id AND quality_score > 0
    ),
    completed_projects = (
        SELECT COUNT(*)
        FROM projects
        WHERE batch_id = NEW.batch_id AND status = 'completed'
    )
    WHERE id = NEW.batch_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_batch_quality
AFTER UPDATE OF quality_score, status ON projects
FOR EACH ROW
EXECUTE FUNCTION update_batch_quality_score();
```

---

## Data Access Patterns

**Optimized Queries:**

1. **Dashboard - Recent Batches:**
```sql
SELECT id, name, status, total_projects, completed_projects, average_quality_score, created_at
FROM batches
WHERE user_id = $1 AND status != 'archived'
ORDER BY created_at DESC
LIMIT 10;
```

2. **Batch Detail - All Projects:**
```sql
SELECT p.*, pc.sections, gm.total_cost_eur
FROM projects p
LEFT JOIN project_contents pc ON p.id = pc.project_id
LEFT JOIN generation_metadata gm ON p.id = gm.project_id
WHERE p.batch_id = $1
ORDER BY p.row_number ASC;
```

3. **Cost Tracking - Monthly Spend:**
```sql
SELECT
    DATE_TRUNC('day', created_at) as date,
    COUNT(*) as projects_generated,
    SUM(total_cost_eur) as total_cost
FROM generation_metadata
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY date DESC;
```

---
