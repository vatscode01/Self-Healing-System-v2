# Self-Healing System Monitor

A beginner-friendly Python automation project that continuously monitors system health, detects abnormal conditions, performs safe automated recovery actions, verifies whether the recovery worked, and records every incident for later analysis.

## Problem Statement
System administrators and developers often face repetitive issues (e.g., full disk space, stopped services). Manually monitoring and resolving these issues is tedious. This system aims to automate the detection and recovery pipeline.

## Architecture
- **Monitor:** Fetches system metrics using `psutil`.
- **Rule Engine:** Detects threshold violations and generates incidents.
- **Recovery Engine:** Executes safe cleanup scripts or Docker container restarts.
- **Verifier:** Verifies system health post-recovery.
- **Database:** SQLite database to persist incidents and actions.
- **Dashboard:** Streamlit app for real-time visualization.

## Features
- CPU, Memory, Disk, and Process monitoring.
- Controlled Docker test service failure simulation.
- Configurable thresholds via `config.json`.
- Streamlit dashboard for monitoring and incident management.
- Full incident lifecycle tracking (Open -> Investigating -> Recovering -> Resolved/Failed).

## Technology Stack
- **Language:** Python
- **Libraries:** psutil, Streamlit, Docker SDK, requests
- **Database:** SQLite
- **Environment:** macOS / Docker

## Installation Instructions

1. **Clone or navigate to the repository:**
   ```bash
   cd self-healing-monitor
   ```

2. **Run using Docker Compose (Recommended):**
   ```bash
   docker compose up --build
   ```

3. **Run Locally (Requires Python 3.9+):**
   ```bash
   pip install -r requirements.txt
   # Start the monitor in one terminal
   python -m app.main
   # Start the dashboard in another terminal
   streamlit run dashboard/dashboard.py
   ```

## Docker Instructions
The project uses `docker-compose` to spin up three services:
1. `test-service`: A mock service for testing service downtime recovery.
2. `monitor`: The main system monitor logic.
3. `dashboard`: Streamlit dashboard exposed on port 8501.

To deliberately cause a failure, stop the test service:
```bash
docker stop test-service
```
Observe the monitor automatically detecting the failure and attempting to restart it!

## Example Failure Scenario
1. `docker compose up -d`
2. Open dashboard on `http://localhost:8501`. Test service is HEALTHY.
3. Run `docker stop test-service`.
4. Monitor detects `SERVICE_DOWN`, logs the incident as `CRITICAL`, and triggers the `RECOVERING` state.
5. Recovery Engine runs `docker start test-service`.
6. Verifier confirms `/health` endpoint returns 200.
7. Incident state set to `RESOLVED` and updated on dashboard.
