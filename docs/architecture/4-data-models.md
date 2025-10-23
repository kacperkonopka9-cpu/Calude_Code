# 4. Data Models

Core business entities with shared TypeScript interfaces (in `packages/shared/src/types/`).

## User Model

**Purpose:** Polish tax consultant using the system

```typescript
interface User {
  id: string; // UUID v4
  email: string;
  name: string;
  company?: string;
  createdAt: Date;
  lastLoginAt?: Date;
  preferences: UserPreferences;
}

interface UserPreferences {
  defaultAiModel: 'claude' | 'gpt4';
  language: 'pl';
  notificationsEnabled: boolean;
}
```

**Relationships:** One User has many Batches (1:N)

---

## Batch Model

**Purpose:** Group of 1-20 project cards processed together

```typescript
interface Batch {
  id: string; // UUID v4
  userId: string;
  name: string;
  status: BatchStatus;
  totalProjects: number; // 1-20
  completedProjects: number;
  averageQualityScore: number; // 0-100
  createdAt: Date;
  completedAt?: Date;
  expiresAt: Date; // createdAt + 90 days
}

enum BatchStatus {
  UPLOADING = 'uploading',
  VALIDATING = 'validating',
  VALIDATION_FAILED = 'validation_failed',
  QUEUED = 'queued',
  PROCESSING = 'processing',
  COMPLETED = 'completed',
  PARTIALLY_COMPLETED = 'partially_completed',
  ARCHIVED = 'archived'
}
```

**Relationships:** Batch belongs to User (N:1), has many Projects (1:N)

---

## Project Model

**Purpose:** Individual R&D project card

```typescript
interface Project {
  id: string;
  batchId: string;
  rowNumber: number; // 1-20 from Excel
  status: ProjectStatus;
  qualityScore: number; // 0-100
  inputData: ProjectInputData;
  generatedContent?: ProjectContent;
  aiModel: 'claude-3.5-sonnet' | 'gpt-4';
  generationMetadata: GenerationMetadata;
  createdAt: Date;
  generatedAt?: Date;
  editedAt?: Date;
}

enum ProjectStatus {
  PENDING = 'pending',
  GENERATING = 'generating',
  COMPLETED = 'completed',
  FAILED = 'failed',
  REVIEWED = 'reviewed',
  EXPORTED = 'exported'
}

interface ProjectInputData {
  nazwaProjektu: string;
  opis: string; // ≥100 chars
  dataRozpoczecia: Date;
  dataZakonczenia: Date;
  celProjektu: string; // ≥50 chars
  osobaOdpowiedzialna: string;
}
```

---

## ProjectContent Model

**Purpose:** Generated content for 8 Ulga B+R sections

```typescript
interface ProjectContent {
  projectId: string;
  sections: Record<SectionKey, SectionContent>;
  version: number;
  lastEditedSection?: SectionKey;
}

enum SectionKey {
  NAZWA_PROJEKTU = 'nazwa_projektu',
  CEL_PROJEKTU = 'cel_projektu',
  OPIS_PROJEKTU = 'opis_projektu',
  NOWATORSTWO = 'nowatorstwo',
  METODOLOGIA = 'metodologia',
  REZULTATY = 'rezultaty',
  KOSZTY = 'koszty',
  HARMONOGRAM = 'harmonogram'
}

interface SectionContent {
  key: SectionKey;
  text: string; // Polish markdown
  isAiGenerated: boolean; // true = yellow, false = white
  qualityScore: number; // 0-100
  characterCount: number;
  generatedAt?: Date;
  editedAt?: Date;
  editedBy?: 'consultant' | 'ai-regeneration';
}
```

---

## GenerationMetadata Model

**Purpose:** Track AI usage for cost monitoring (FR20)

```typescript
interface GenerationMetadata {
  projectId: string;
  attempts: number; // 1-3
  totalInputTokens: number;
  totalOutputTokens: number;
  totalCostEur: number;
  averageLatencyMs: number;
  modelUsed: 'claude-3.5-sonnet' | 'gpt-4';
  errors: ApiError[];
  completedAt?: Date;
}

interface ApiError {
  timestamp: Date;
  errorCode: string;
  errorMessage: string;
  retryable: boolean;
}
```

---

## ValidationError Model

**Purpose:** Excel validation errors (FR3)

```typescript
interface ValidationError {
  batchId: string;
  rowNumber: number;
  columnName: string;
  errorType: ValidationErrorType;
  errorMessage: string; // Polish
}

enum ValidationErrorType {
  MISSING_REQUIRED = 'missing_required',
  INVALID_TYPE = 'invalid_type',
  MIN_LENGTH = 'min_length',
  INVALID_DATE = 'invalid_date',
  DATE_LOGIC_ERROR = 'date_logic_error'
}
```

---

## ExportHistory Model

**Purpose:** Track Word exports for audit

```typescript
interface ExportHistory {
  id: string;
  projectId: string;
  userId: string;
  fileName: string; // "Projekt-{Name}-{Date}.docx"
  s3Key: string;
  fileSizeBytes: number;
  exportedAt: Date;
  expiresAt: Date; // exportedAt + 30 days
}
```

---
