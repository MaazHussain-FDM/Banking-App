# /speckit.clarify

## Clarifications and Decisions
1. **Data store**: SQLite is acceptable for this project and interview demo.
2. **Authentication**: built-in Django auth is sufficient.
3. **Currency handling**: use decimal fields with 2 decimal places.
4. **Coverage target**: minimum 80% in CI.
5. **Quality gate authority**: Sonar Quality Gate determines release readiness.
6. **Deployment target**: self-hosted Windows runner for GitHub Actions deployment job.

## Risks
- Deployment job needs a configured self-hosted Windows runner.
- Sonar integration requires valid repository secrets and project key.

