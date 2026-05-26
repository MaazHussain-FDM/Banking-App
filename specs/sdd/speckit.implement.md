# /speckit.implement

## Execution Runbook

## 1) Local implementation
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 2) Push and CI quality checks
1. Push branch to GitHub.
2. Open PR.
3. CI runs tests and coverage threshold checks.

## 3) Sonar quality governance
1. Configure repo secrets: `SONAR_TOKEN`, optional `SONAR_HOST_URL`.
2. Set `sonar.projectKey` in `sonar-project.properties`.
3. Verify Sonar scan and Quality Gate status on PR.

## 4) Deployment
1. Deploy from `main` only after quality gate pass.
2. Run Waitress:
```powershell
.\scripts\run_waitress.ps1 -Host 0.0.0.0 -Port 8000
```
3. Optional Windows service mode:
```powershell
.\scripts\install_nssm_service.ps1 -NssmPath "C:\tools\nssm\nssm.exe"
```

