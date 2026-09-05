# Flask psutil metrics dashboard

A small Flask app that reads CPU, RAM, and disk metrics with `psutil` and displays them in an auto-refreshing HTML dashboard.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser.

## Run with Docker

```powershell
docker build -t flask-psutil-dashboard .
docker run --rm -p 5000:5000 flask-psutil-dashboard
```

Open http://localhost:5000 in your browser.

## Endpoints

- `/` - auto-refreshing dashboard
- `/api/metrics` - JSON metrics
- `/health` - simple health check
