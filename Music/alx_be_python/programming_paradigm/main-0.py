import sys
from bank_account import BankAccount


def main():
    # Initialize a bank account with an example starting balance
    account = BankAccount(100.0)

    # If no command-line argument is provided, display usage instructions
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Split the command and optional amount from the command-line argument
    command, *params = sys.argv[1].split(':')

    # If there's an amount provided, convert it to a float, otherwise set to None
    amount = float(params[0]) if params else None

    # Execute the corresponding banking operation
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount: .2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount: .2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
