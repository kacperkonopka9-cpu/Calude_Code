# R&D Tax Relief API

Backend API dla Generatora Kart Projektów Ulga B+R (R&D Tax Relief Project Card Generator).

## Tech Stack

- **Python 3.11+**
- **FastAPI 0.104+** - Modern async web framework
- **openpyxl 3.1+** - Excel file generation
- **pytest 7.4+** - Testing framework
- **uvicorn 0.24+** - ASGI server

## Setup

### 1. Create Virtual Environment

```bash
cd apps/api
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env if needed
```

## Development

### Run API Server

```bash
# From apps/api directory
source venv/bin/activate
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

API will be available at:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Run Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/
```

### Code Quality

```bash
# Type checking
mypy src/

# Linting
ruff check src/ tests/

# Format code
ruff format src/ tests/
```

## API Endpoints

### GET /v1/templates/excel

Download Excel template for R&D project data.

**Response:**
- Content-Type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Filename: `Szablon-Ulga-BR.xlsx`

**Template Structure:**
- Sheet 1: "Dane projektów" (6 Polish columns with example data)
- Sheet 2: "Instrukcje" (Polish field descriptions)

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Project Structure

```
apps/api/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration
│   ├── routes/
│   │   └── templates.py     # Template endpoints
│   └── services/
│       └── template_service.py  # Excel generation logic
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   └── services/
│   │       └── test_template_service.py
│   └── integration/
│       └── test_templates_api.py
├── pyproject.toml
├── requirements.txt
├── .env.example
└── README.md
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_HOST` | `0.0.0.0` | API server host |
| `API_PORT` | `8000` | API server port |
| `FRONTEND_URL` | `http://localhost:5173` | Frontend URL for CORS |
| `API_RELOAD` | `true` | Auto-reload on code changes |
