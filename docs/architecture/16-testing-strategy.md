# 16. Testing Strategy

## 16.1 Testing Pyramid

```
        E2E Tests (Playwright)
       /                      \
  Integration Tests
 /            |             \
Frontend Unit  Backend Unit  Worker Unit
```

---

## 16.2 Test Organization

**Frontend Tests:**

```
apps/web/tests/
├── unit/
│   ├── components/
│   │   ├── QualityScoreBadge.test.tsx
│   │   └── ProjectCard.test.tsx
│   └── hooks/
│       └── useAuth.test.ts
├── integration/
│   ├── BatchUpload.test.tsx
│   └── ProjectReview.test.tsx
└── e2e/
    ├── complete-workflow.spec.ts
    └── batch-processing.spec.ts
```

**Backend Tests:**

```
apps/api/tests/
├── unit/
│   ├── services/
│   │   ├── test_ai_service.py
│   │   └── test_validation_service.py
│   └── repositories/
│       └── test_batch_repository.py
├── integration/
│   ├── test_batches_api.py
│   ├── test_projects_api.py
│   └── test_auth_api.py
└── e2e/
    └── test_complete_workflow.py
```

---

## 16.3 Test Examples

**Frontend Component Test:**

```typescript
// apps/web/tests/unit/components/QualityScoreBadge.test.tsx
import { render, screen } from '@testing-library/react';
import { QualityScoreBadge } from '@/components/molecules/QualityScoreBadge';

describe('QualityScoreBadge', () => {
  it('displays score with correct color for high quality', () => {
    render(<QualityScoreBadge score={85} />);
    const badge = screen.getByText('85%');
    expect(badge).toBeInTheDocument();
    expect(badge).toHaveClass('MuiBadge-colorSuccess');
  });

  it('displays warning color for medium quality', () => {
    render(<QualityScoreBadge score={65} />);
    const badge = screen.getByText('65%');
    expect(badge).toHaveClass('MuiBadge-colorWarning');
  });

  it('displays error color for low quality', () => {
    render(<QualityScoreBadge score={40} />);
    const badge = screen.getByText('40%');
    expect(badge).toHaveClass('MuiBadge-colorError');
  });
});
```

**Backend API Test:**

```python
# apps/api/tests/integration/test_batches_api.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_create_batch_with_valid_excel(client: AsyncClient, auth_token: str):
    files = {'file': ('test.xlsx', open('tests/fixtures/valid.xlsx', 'rb'))}
    data = {'name': 'Test Batch'}

    response = await client.post(
        '/v1/batches',
        files=files,
        data=data,
        headers={'Authorization': f'Bearer {auth_token}'}
    )

    assert response.status_code == 201
    batch = response.json()
    assert batch['name'] == 'Test Batch'
    assert batch['status'] == 'queued'
    assert batch['totalProjects'] == 5

@pytest.mark.asyncio
async def test_create_batch_with_invalid_excel_returns_validation_errors(
    client: AsyncClient,
    auth_token: str
):
    files = {'file': ('invalid.xlsx', open('tests/fixtures/invalid.xlsx', 'rb'))}
    data = {'name': 'Invalid Batch'}

    response = await client.post(
        '/v1/batches',
        files=files,
        data=data,
        headers={'Authorization': f'Bearer {auth_token}'}
    )

    assert response.status_code == 400
    errors = response.json()['errors']
    assert len(errors) > 0
    assert errors[0]['rowNumber'] == 2
    assert errors[0]['errorType'] == 'missing_required'
```

**E2E Test:**

```typescript
// apps/web/tests/e2e/complete-workflow.spec.ts
import { test, expect } from '@playwright/test';

test('complete batch processing workflow', async ({ page }) => {
  // Login
  await page.goto('http://localhost:5173/login');
  await page.fill('input[name="email"]', 'test@example.com');
  await page.fill('input[name="password"]', 'TestPass123');
  await page.click('button[type="submit"]');

  // Wait for dashboard
  await expect(page).toHaveURL(/.*dashboard/);

  // Upload Excel file
  await page.click('text=Nowa partia');
  const fileInput = await page.locator('input[type="file"]');
  await fileInput.setInputFiles('tests/fixtures/valid.xlsx');
  await page.fill('input[name="batchName"]', 'E2E Test Batch');
  await page.click('button:has-text("Rozpocznij generowanie")');

  // Wait for processing screen
  await expect(page).toHaveURL(/.*processing/);

  // Wait for first project to complete (max 2 minutes)
  await expect(page.locator('text=Gotowe').first()).toBeVisible({ timeout: 120000 });

  // Navigate to review
  await page.click('.project-card >> nth=0');
  await expect(page).toHaveURL(/.*review/);

  // Verify sections loaded
  await expect(page.locator('text=Nazwa projektu')).toBeVisible();
  await expect(page.locator('text=Cel projektu')).toBeVisible();

  // Edit section
  const editor = page.locator('.tiptap-editor').first();
  await editor.click();
  await editor.type(' - edycja testowa');

  // Wait for quality score update
  await page.waitForTimeout(1000);

  // Export project
  await page.click('button:has-text("Pobierz projekt")');

  // Verify download started
  const download = await page.waitForEvent('download');
  expect(download.suggestedFilename()).toMatch(/Projekt-.*\.docx/);
});
```

---
