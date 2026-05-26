# /speckit.plan

## Implementation Plan
1. Scaffold Django project and banking app.
2. Implement models, forms, views, URLs, and templates.
3. Add tests for deposit, withdraw, overdraft rejection, transaction creation.
4. Add CI workflow (install, migrate, test, coverage).
5. Add Sonar workflow (scan + quality gate).
6. Add deployment scripts for Windows (Waitress + optional NSSM).
7. Document runbook and interview-friendly architecture mapping.

## Quality Gates
1. Unit tests pass.
2. Coverage threshold met.
3. Sonar Quality Gate passes.
4. Deployment scripts are runnable on target host.

