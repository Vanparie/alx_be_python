class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a new bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the given amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        """Withdraw the given amount if sufficient funds are available."""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive")
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance: .2f}")
