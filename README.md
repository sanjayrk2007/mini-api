# mini-api

A minimal FastAPI backend with two JSON endpoints.

## Endpoints

| Method | Path      | Description                          |
|--------|-----------|---------------------------------------|
| GET    | `/health` | Returns server status                 |
| GET    | `/hello`  | Returns a greeting (optional `name`)  |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

## Run

```bash
uvicorn main:app --reload
```

Server runs at `http://127.0.0.1:8000`.

## Test

```bash
curl http://127.0.0.1:8000/health
curl "http://127.0.0.1:8000/hello?name=Sanjay"
```

Or open in browser:
- `http://127.0.0.1:8000/hello?name=Sanjay`
- `http://127.0.0.1:8000/docs` (interactive Swagger UI)

## Tech

FastAPI + Uvicorn