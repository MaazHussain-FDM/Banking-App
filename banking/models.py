from decimal import Decimal, InvalidOperation

from django.contrib.auth.models import User
from django.db import models, transaction as db_transaction


class Transaction(models.Model):
    class Type(models.TextChoices):
        DEPOSIT = "DEPOSIT", "Deposit"
        WITHDRAWAL = "WITHDRAWAL", "Withdrawal"

    account = models.ForeignKey(
        "BankAccount",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    transaction_type = models.CharField(max_length=20, choices=Type.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at", "-id")


class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bank_account")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.balance}"

    @staticmethod
    def _normalize_amount(amount: Decimal) -> Decimal:
        try:
            normalized = Decimal(str(amount)).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError, TypeError) as exc:
            raise ValueError("Amount must be a valid decimal value.") from exc
        if normalized <= 0:
            raise ValueError("Amount must be greater than zero.")
        return normalized

    @db_transaction.atomic
    def deposit(self, amount: Decimal) -> Transaction:
        normalized = self._normalize_amount(amount)
        self.balance = (self.balance + normalized).quantize(Decimal("0.01"))
        self.save(update_fields=["balance"])
        return Transaction.objects.create(
            account=self,
            transaction_type=Transaction.Type.DEPOSIT,
            amount=normalized,
        )

    @db_transaction.atomic
    def withdraw(self, amount: Decimal) -> Transaction:
        normalized = self._normalize_amount(amount)
        if normalized > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance = (self.balance - normalized).quantize(Decimal("0.01"))
        self.save(update_fields=["balance"])
        return Transaction.objects.create(
            account=self,
            transaction_type=Transaction.Type.WITHDRAWAL,
            amount=normalized,
        )

