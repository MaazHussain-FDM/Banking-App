# Django Banking App (SDD + SonarQube + CI/CD + Windows Deployment)

This repository is set up to demonstrate the full delivery workflow:

1. Specification-driven development (SDD) with Spec Kit commands.
2. Minimal Django banking implementation (UI + rules + data).
3. Automated test and coverage checks in GitHub Actions.
4. SonarQube/SonarCloud scanning and Quality Gate enforcement.
5. Deployment on Windows using Waitress (optional NSSM service).

## 1) SDD workflow (Spec Kit command order)

Run these in order:

1. `/speckit.constitution`
2. `/speckit.specify`
3. `/speckit.clarify`
4. `/speckit.checklist`
5. `/speckit.plan`
6. `/speckit.tasks`
7. `/speckit.analyze`
8. `/speckit.implement`

SDD artifact files are stored in:

`specs/sdd/`

## 2) Local setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## 3) Run the application

### Option A: Django development server

```powershell
.venv\Scripts\Activate.ps1
python manage.py runserver
```

Open: `http://127.0.0.1:8000/` or `http://localhost:8000/`

### Option B: Waitress (production-style local run)

```powershell
.venv\Scripts\Activate.ps1
.\scripts\run_waitress.ps1 -ListenHost 0.0.0.0 -Port 8000
```

Open from same machine: `http://127.0.0.1:8000/`  
(`0.0.0.0` is a bind address, not a browser URL.)

## 4) Implemented architecture layers

| Layer | Responsibility | Implementation |
| --- | --- | --- |
| User interface | Register + banking actions | Django templates and views |
| Business logic | Banking rules and validation | `BankAccount.deposit` and `BankAccount.withdraw` |
| Data layer | Persist accounts and transactions | SQLite with `BankAccount` and `Transaction` models |
| Testing | Prove critical behavior | `pytest` tests in `banking/tests.py` |
| CI/CD | Repeatable checks on push/PR | `.github/workflows/ci.yml` |
| Quality analysis | Bugs, smells, vulnerabilities, coverage | `.github/workflows/sonar.yml` + `sonar-project.properties` |
| Deployment | Windows app hosting | `scripts/run_waitress.ps1` and optional `install_nssm_service.ps1` |

## 5) GitHub Actions pipeline

`ci.yml` performs:

1. Dependency install
2. Django migration
3. Tests with coverage
4. Coverage threshold enforcement (`--fail-under=80`)

## 6) SonarQube/SonarCloud quality gate

`sonar.yml` performs:

1. Test run + `coverage.xml` generation
2. Sonar scan publishing
3. Quality Gate check (pass/fail)

Repository secrets needed:

- `SONAR_TOKEN` (required)
- `SONAR_HOST_URL` (optional; set for SonarQube Server, omit for SonarCloud)

Also update `sonar-project.properties`:

- `sonar.projectKey`
- optionally add `sonar.organization` if using SonarCloud

## 7) Windows deployment

### Run directly with Waitress

```powershell
.venv\Scripts\Activate.ps1
.\scripts\run_waitress.ps1 -ListenHost 0.0.0.0 -Port 8000
```

### Optional: run as a Windows Service (NSSM)

```powershell
.\scripts\install_nssm_service.ps1 -NssmPath "C:\tools\nssm\nssm.exe"
```

## 8) Merge/deploy decision workflow

1. Push branch and open PR.
2. CI workflow runs tests + coverage.
3. Sonar workflow publishes analysis.
4. Quality Gate result drives decision:
   - **Pass** → merge/deploy
   - **Fail** → create improvement tasks and iterate

