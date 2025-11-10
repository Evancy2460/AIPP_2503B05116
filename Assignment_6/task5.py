class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        """Initialize the account with an optional starting balance."""
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= float(amount)

    def balance(self) -> float:
        """Return the current account balance."""
        return self._balance

if __name__ == "__main__":
    # Interactive demonstration using keyboard input
    try:
        initial_amount = float(input("Enter initial balance: "))
        account = BankAccount(initial_amount)

        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)

        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)
    except ValueError as exc:
        print(f"Error: {exc}")
    else:
        print(f"Final balance: {account.balance()}")

