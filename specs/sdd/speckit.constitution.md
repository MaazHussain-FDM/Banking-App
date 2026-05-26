# /speckit.constitution

## Purpose
Define the non-negotiable engineering and quality rules for this repository.

## Project Constitution
1. **Quality gate before merge/deploy**: code must pass CI and Sonar Quality Gate.
2. **Tests are mandatory**: banking rules require automated tests for happy path and rejection path.
3. **Security-first defaults**: no secrets in repo, production runs with `DJANGO_DEBUG=0`.
4. **Traceable delivery**: each feature/task links to spec and implementation evidence.
5. **Small, reversible changes**: prefer PRs that are easy to review and rollback.

## Acceptance Policy
- Merge is blocked on failed tests, failed coverage threshold, or failed Sonar gate.
- Deployment is allowed only from `main` after quality checks pass.

