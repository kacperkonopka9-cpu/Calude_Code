# R&D Tax Relief Generator - Frontend

React 18 TypeScript frontend for the R&D Tax Relief Project Card Generator.

## Tech Stack

- **React** 18.2+ with TypeScript 5.3+
- **Vite** 5.0+ (build tool)
- **Material-UI** 5.14+ (UI components with custom iNOV theme)
- **Tailwind CSS** 3.3+ (utility-first styling)
- **Vitest** + React Testing Library (testing)
- **Atomic Design** pattern (component organization)

## Setup

```bash
# Install dependencies
npm install

# Start development server (port 5173)
npm run dev

# Run tests
npm test

# Build for production
npm run build

# Type check
npm run type-check

# Lint code
npm run lint
```

## Environment Variables

Copy `.env.example` to `.env.local` and configure:

```bash
VITE_API_BASE_URL=http://localhost:8000/v1
VITE_WS_URL=ws://localhost:8000/ws
VITE_COGNITO_USER_POOL_ID=eu-central-1_XXXXXXXXX
VITE_COGNITO_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXX
VITE_AWS_REGION=eu-central-1
```

## Project Structure

```
src/
├── components/
│   ├── atoms/         # Smallest UI elements
│   ├── molecules/     # Combinations of atoms
│   ├── organisms/     # Complex UI sections
│   └── templates/     # Page layouts
├── pages/
│   ├── Dashboard/
│   ├── Upload/
│   ├── Processing/
│   ├── Review/
│   └── Login/
├── hooks/            # Custom React hooks
├── services/         # API client layer
├── stores/           # Global state
├── styles/           # Theme and global CSS
├── utils/            # Helper functions
├── config.ts         # Environment config
└── App.tsx
```

## iNOV Brand Theme

- **Primary**: Yellow #F5C344
- **Secondary**: Navy #2C3E50
- **Typography**: Inter (UI), Roboto Slab (headings)

## Coding Standards

- **Components**: PascalCase (e.g., `UserProfile.tsx`)
- **Hooks**: camelCase with 'use' prefix (e.g., `useAuth.ts`)
- **Functions**: camelCase
- **Constants**: UPPER_SNAKE_CASE
- **Interfaces/Types**: PascalCase

Never access `import.meta.env` directly - always use `src/config.ts`.
