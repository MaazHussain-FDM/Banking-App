# /speckit.specify

## Product Goal
Deliver a minimal Django banking app that demonstrates full system delivery workflow from specification to deployment.

## Functional Scope
1. User can register and log in.
2. User can view current account balance.
3. User can deposit money.
4. User can withdraw money.
5. Withdrawal fails when amount is greater than balance.
6. User can view transaction history.

## Non-Functional Scope
1. Repeatable CI on every push/PR.
2. Coverage reporting and threshold enforcement.
3. Sonar analysis and Quality Gate.
4. Windows deployment via Waitress (optional NSSM service).

## Out of Scope
- Multi-account transfers
- Complex authorization roles
- External payment integration

