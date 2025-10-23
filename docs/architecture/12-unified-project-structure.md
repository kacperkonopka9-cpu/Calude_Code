# 12. Unified Project Structure

Full monorepo structure with all packages:

```
rnd-tax-relief-generator/
├── .github/
│   └── workflows/
│       ├── ci.yaml                 # Run tests on PR
│       └── deploy.yaml             # Deploy to AWS
├── apps/
│   ├── web/                        # React frontend
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── atoms/
│   │   │   │   ├── molecules/
│   │   │   │   ├── organisms/
│   │   │   │   └── templates/
│   │   │   ├── pages/
│   │   │   │   ├── Dashboard/
│   │   │   │   ├── Upload/
│   │   │   │   ├── Processing/
│   │   │   │   ├── Review/
│   │   │   │   └── Login/
│   │   │   ├── hooks/
│   │   │   ├── services/
│   │   │   ├── stores/
│   │   │   ├── styles/
│   │   │   ├── utils/
│   │   │   ├── App.tsx
│   │   │   └── main.tsx
│   │   ├── public/
│   │   ├── tests/
│   │   ├── index.html
│   │   ├── vite.config.ts
│   │   ├── tsconfig.json
│   │   └── package.json
│   └── api/                        # FastAPI backend
│       ├── src/
│       │   ├── routes/
│       │   ├── services/
│       │   ├── repositories/
│       │   ├── models/
│       │   ├── schemas/
│       │   ├── workers/
│       │   │   ├── celery_app.py
│       │   │   ├── ai_generation_task.py
│       │   │   └── export_task.py
│       │   ├── middleware/
│       │   ├── utils/
│       │   ├── main.py
│       │   └── config.py
│       ├── tests/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── pyproject.toml
├── packages/
│   ├── shared/                     # Shared TypeScript types
│   │   ├── src/
│   │   │   ├── types/
│   │   │   │   ├── user.ts
│   │   │   │   ├── batch.ts
│   │   │   │   ├── project.ts
│   │   │   │   └── index.ts
│   │   │   └── constants/
│   │   ├── tsconfig.json
│   │   └── package.json
│   └── config/                     # Shared configs
│       ├── eslint/
│       ├── typescript/
│       └── jest/
├── infrastructure/                 # AWS CDK
│   ├── lib/
│   │   ├── database-stack.ts
│   │   ├── api-stack.ts
│   │   ├── frontend-stack.ts
│   │   └── monitoring-stack.ts
│   ├── bin/
│   │   └── app.ts
│   ├── cdk.json
│   └── tsconfig.json
├── scripts/                        # Build/deploy scripts
│   ├── deploy.sh
│   └── local-dev.sh
├── docs/                          # Documentation
│   ├── prd.md
│   ├── architecture.md
│   ├── front-end-spec.md
│   └── api-docs.md
├── .env.example
├── .gitignore
├── package.json                   # Root package.json
├── tsconfig.json                  # Root TypeScript config
└── README.md
```

---
