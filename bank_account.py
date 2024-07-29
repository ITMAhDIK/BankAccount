from typing import List


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
    ----------
    all_account_numbers : List[int]
        A class-level list to keep track of all unique account numbers.
    last_account_number : int
        A class-level variable to keep track of the last assigned account number.
    account_number : int
        The unique account number for this bank account.
    name : str
        The name of the account holder.
    balance : float
        The current balance of the account.

    Methods:
    -------
    display() -> None:
        Displays the account holder's name and current balance.
    deposit(amount: float) -> None:
        Deposits a specified amount into the account and displays the updated balance.
    withdraw(amount: float) -> None:
        Withdraws a specified amount from the account if sufficient funds are available and displays the updated balance.
    """

    all_account_numbers: List[int] = []
    last_account_number = 999

    def __init__(self, name: str) -> None:
        """
        Constructs all the necessary attributes for the BankAccount object.

        Parameters:
        ----------
        name : str
            The name of the account holder.
        """
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_numbers.append(an)
        self.name = name
        self.balance: float = 0.0

    def display(self) -> None:
        """
        Displays the account holder's name and current balance.
        """
        print("*" * 40)
        print(f"Hi {self.name}\nyour current balance: {self.balance}")
        print("*" * 40)

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the account and displays the updated balance.

        Parameters:
        ----------
        amount : float
            The amount to deposit.
        """
        self.balance += amount
        self.display()

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account if sufficient funds are available and displays the updated balance.

        Parameters:
        ----------
        amount : float
            The amount to withdraw.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("KHO KIRI")
        self.display()


def main():
    """
    Main function to run the bank account management program.
    """
    account1 = BankAccount("Mahdi Karimi")
    print("*" * 40)
    print(f"This is your account number: {account1.account_number}")
    account1.display()
    while True:
        choice = int(input("Enter your choice:\n"
                           "1 to see your balance\n"
                           "2 to deposit money\n"
                           "3 to withdraw money\n"
                           "4 to exit...\n"
                           "Your choice: "))
        if choice == 1:
            account1.display()
        elif choice == 2:
            amount = float(input("Please enter the amount to deposit: "))
            account1.deposit(amount)
        elif choice == 3:
            amount = float(input("Please enter the amount to withdraw: "))
            account1.withdraw(amount)
        elif choice == 4:
            break
        else:
            print("KHO KIRI")


if __name__ == "__main__":
    main()
