from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AmountForm, UserRegisterForm
from .models import BankAccount


def register_view(request):
    if request.user.is_authenticated:
        return redirect("account-detail")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            BankAccount.objects.create(user=user)
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("account-detail")
    else:
        form = UserRegisterForm()

    return render(request, "banking/register.html", {"form": form})


@login_required
def account_detail(request):
    account, _ = BankAccount.objects.get_or_create(user=request.user)
    return render(request, "banking/account_detail.html", {"account": account})


@login_required
def deposit_view(request):
    account, _ = BankAccount.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AmountForm(request.POST)
        if form.is_valid():
            account.deposit(form.cleaned_data["amount"])
            messages.success(request, "Deposit completed.")
            return redirect("account-detail")
    else:
        form = AmountForm()
    return render(request, "banking/amount_form.html", {"form": form, "title": "Deposit"})


@login_required
def withdraw_view(request):
    account, _ = BankAccount.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AmountForm(request.POST)
        if form.is_valid():
            try:
                account.withdraw(form.cleaned_data["amount"])
            except ValueError as exc:
                messages.error(request, str(exc))
            else:
                messages.success(request, "Withdrawal completed.")
                return redirect("account-detail")
    else:
        form = AmountForm()
    return render(request, "banking/amount_form.html", {"form": form, "title": "Withdraw"})


@login_required
def transaction_list_view(request):
    account, _ = BankAccount.objects.get_or_create(user=request.user)
    transactions = account.transactions.all()
    return render(request, "banking/transactions.html", {"transactions": transactions})

