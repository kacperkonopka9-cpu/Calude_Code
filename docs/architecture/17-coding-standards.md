# 17. Coding Standards

## 17.1 Critical Fullstack Rules

**Type Sharing:** Always define types in `packages/shared` and import from there. Never duplicate type definitions between frontend and backend.

**API Calls:** Never make direct HTTP calls in components - use the service layer (`apps/web/src/services/`).

**Environment Variables:** Access only through config objects, never `process.env` or `import.meta.env` directly.

**Error Handling:** All API routes must use the standard error handler middleware.

**State Updates:** Never mutate state directly - use proper state management patterns (React Query mutations, setState).

**Database Access:** Never write raw SQL - use SQLAlchemy ORM and repository pattern.

**AI Prompts:** Store all prompts as constants in `apps/api/src/services/prompts/`, never inline.

**S3 Keys:** Use consistent naming: `{userId}/{batchId}/uploads/{filename}` for uploads, `{userId}/{batchId}/exports/{projectId}.docx` for exports.

---

## 17.2 Naming Conventions

| Element | Frontend | Backend | Example |
|---------|----------|---------|---------|
| **Components** | PascalCase | - | `UserProfile.tsx` |
| **Hooks** | camelCase with 'use' | - | `useAuth.ts` |
| **API Routes** | - | snake_case | `/api/user-profile` |
| **Database Tables** | - | snake_case | `user_profiles` |
| **Functions** | camelCase | snake_case | `handleSubmit()`, `validate_excel()` |
| **Constants** | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE | `MAX_BATCH_SIZE` |
| **Interfaces/Types** | PascalCase | PascalCase | `UserProfile` |

---

## 17.3 Code Quality Gates

**Pre-commit Requirements:**
- ESLint passes (frontend)
- Ruff/mypy passes (backend)
- Unit tests pass
- Type checking passes

**Pre-merge Requirements:**
- All tests pass (unit + integration)
- Code coverage ≥80% for new code
- No TypeScript/mypy errors
- PR reviewed by at least 1 developer

---
