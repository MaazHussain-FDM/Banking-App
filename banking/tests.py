from decimal import Decimal

import pytest
from django.contrib.auth.models import User

from .models import BankAccount, Transaction

pytestmark = pytest.mark.django_db


@pytest.fixture
def account():
    user = User.objects.create_user(
        username="alice",
        password="Password123!",
        email="alice@example.com",
    )
    return BankAccount.objects.create(user=user)


def test_deposit_increases_balance_and_creates_transaction(account):
    transaction = account.deposit(Decimal("100.00"))
    account.refresh_from_db()

    assert account.balance == Decimal("100.00")
    assert transaction.transaction_type == Transaction.Type.DEPOSIT
    assert transaction.amount == Decimal("100.00")
    assert account.transactions.count() == 1


def test_withdrawal_reduces_balance(account):
    account.deposit(Decimal("200.00"))
    transaction = account.withdraw(Decimal("50.00"))
    account.refresh_from_db()

    assert account.balance == Decimal("150.00")
    assert transaction.transaction_type == Transaction.Type.WITHDRAWAL
    assert transaction.amount == Decimal("50.00")


def test_overdraft_is_rejected(account):
    account.deposit(Decimal("40.00"))

    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(Decimal("50.00"))


def test_transactions_are_recorded_for_each_operation(account):
    account.deposit(Decimal("20.00"))
    account.withdraw(Decimal("10.00"))

    transactions = list(account.transactions.values_list("transaction_type", "amount"))
    assert len(transactions) == 2
    assert ("DEPOSIT", Decimal("20.00")) in transactions
    assert ("WITHDRAWAL", Decimal("10.00")) in transactions

