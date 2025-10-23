# 10. Frontend Architecture

## 10.1 Component Architecture

**Organization:** Atomic Design pattern

```
apps/web/src/
├── components/
│   ├── atoms/              # Basic building blocks
│   │   ├── Button/
│   │   ├── Input/
│   │   ├── Badge/
│   │   └── Spinner/
│   ├── molecules/          # Simple component groups
│   │   ├── ProjectCard/
│   │   ├── QualityScoreBadge/
│   │   ├── FileUploadZone/
│   │   └── SectionEditor/
│   ├── organisms/          # Complex components
│   │   ├── BatchGrid/
│   │   ├── ProjectList/
│   │   ├── ReviewPanel/
│   │   └── NavigationBar/
│   └── templates/          # Page layouts
│       ├── DashboardLayout/
│       └── AuthLayout/
├── pages/                  # Route components
│   ├── Dashboard/
│   ├── Upload/
│   ├── Processing/
│   ├── Review/
│   └── Login/
├── hooks/                  # Custom React hooks
│   ├── useAuth.ts
│   ├── useBatch.ts
│   ├── useWebSocket.ts
│   └── useProjects.ts
├── services/               # API client
│   ├── api.ts             # Axios instance
│   ├── batches.ts
│   ├── projects.ts
│   └── auth.ts
├── stores/                 # Global state (minimal)
│   └── authStore.ts       # Auth context only
├── styles/                 # Global styles
│   ├── theme.ts           # MUI iNOV theme
│   └── globals.css
└── utils/                  # Utilities
    ├── formatters.ts
    └── validators.ts
```

**Component Template Example:**

```typescript
// apps/web/src/components/molecules/QualityScoreBadge/QualityScoreBadge.tsx
import { Badge } from '@mui/material';
import { FC } from 'react';

interface QualityScoreBadgeProps {
  score: number; // 0-100
  size?: 'small' | 'medium' | 'large';
}

export const QualityScoreBadge: FC<QualityScoreBadgeProps> = ({
  score,
  size = 'medium'
}) => {
  const getColor = (score: number) => {
    if (score < 50) return 'error';
    if (score < 70) return 'warning';
    return 'success';
  };

  return (
    <Badge
      badgeContent={`${Math.round(score)}%`}
      color={getColor(score)}
      sx={{
        fontSize: size === 'large' ? '1.2rem' : '0.875rem',
        fontWeight: 600
      }}
    />
  );
};
```

---

## 10.2 State Management Architecture

**State Structure:**

```typescript
// Global State (React Context)
interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

// Server State (React Query)
// Managed automatically by React Query hooks

// Local Component State
// Managed by useState/useReducer within components
```

**State Management Patterns:**

1. **Authentication:** React Context (`AuthProvider`)
2. **Server Data:** React Query (batches, projects, API calls)
3. **WebSocket State:** Custom `useWebSocket` hook with React Query integration
4. **Form State:** React Hook Form with Zod validation
5. **UI State:** Local component state (modals, drawers, etc.)

---

## 10.3 Routing Architecture

**Route Organization:**

```typescript
// apps/web/src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />

        {/* Protected routes */}
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/batches/new" element={<UploadPage />} />
          <Route path="/batches/:batchId/processing" element={<ProcessingPage />} />
          <Route path="/batches/:batchId/review" element={<ReviewPage />} />
          <Route path="/batches/:batchId/review/:projectId" element={<ProjectReviewPage />} />
        </Route>

        {/* 404 */}
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  );
}
```

**Protected Route Pattern:**

```typescript
// apps/web/src/components/ProtectedRoute.tsx
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';

export const ProtectedRoute = () => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
};
```

---

## 10.4 Frontend Services Layer

**API Client Setup:**

```typescript
// apps/web/src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/v1',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor (add JWT token)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor (handle errors)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired, redirect to login
      localStorage.removeItem('auth_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

**Service Example:**

```typescript
// apps/web/src/services/batches.ts
import api from './api';
import { Batch, Project } from '@shared/types';

export const batchesService = {
  async list(limit = 10, offset = 0): Promise<{ batches: Batch[]; total: number }> {
    const { data } = await api.get('/batches', { params: { limit, offset } });
    return data;
  },

  async create(file: File, name: string): Promise<Batch> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('name', name);

    const { data } = await api.post('/batches', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return data;
  },

  async get(batchId: string): Promise<Batch & { projects: Project[] }> {
    const { data } = await api.get(`/batches/${batchId}`);
    return data;
  },

  async startGeneration(batchId: string): Promise<void> {
    await api.post(`/batches/${batchId}/generate`);
  },

  async delete(batchId: string): Promise<void> {
    await api.delete(`/batches/${batchId}`);
  }
};
```

---
