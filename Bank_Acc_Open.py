import random
import pandas as pd
import os
from datetime import datetime


class bank:

    def __init__(self, name, ac_no, bal):
        self.name = name
        self.ac_no = ac_no
        self.bal = bal

        if self.bal < 1000:
            print("Minimum balance of Rs.1000 is required to create account.")
        else:
            print("Account created successfully")


    def deposit(self, amt):
        self.bal = self.bal + amt
        print("Amount deposited successfully")
        print("Your new balance is:", self.bal)


    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient balance")
        else:
            self.bal = self.bal - amt
            print("Withdrawal successful")
            print("Your new balance is:", self.bal)


    def display(self):
        print("\nAccount Information")
        print("Name:", self.name)
        print("Account No:", self.ac_no)
        print("Balance:", self.bal)


    def bal_check(self):
        rate = 0.08
        si = self.bal * rate
        self.bal = self.bal + si
        print("Balance after interest:", self.bal)



# Excel file name
file_name = "Bank3.xlsx"

Accountno = None
b = None


while True:

    print("\n----- BANK MENU -----")
    print("1.Create Account")
    print("2.Account Information")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Check Balance with Interest")
    print("6.Exit")

    n = int(input("Enter choice: "))


    # CREATE ACCOUNT
    if n == 1:

        name = input("Enter your name: ")
        a = float(input("Enter initial deposit: "))

        Accountno = random.randint(100000, 999999)

        b = bank(name, Accountno, a)

        if a >= 1000:

            df = pd.DataFrame({
                "Name":[name],
                "Date": [datetime.now()],
                "Credit/Debit": [a],
                "Balance": [a]
            })

            df.set_index("Date", inplace=True)

            with pd.ExcelWriter(file_name, engine="openpyxl", mode="a" if os.path.exists(file_name) else "w") as writer:
                df.to_excel(writer, sheet_name=str(Accountno))

            print("Your Account Number:", Accountno)



    # ACCOUNT INFO
    elif n == 2:

        if b:
            b.display()
        else:
            print("Create account first")



    # DEPOSIT
    elif n == 3:

        if b:

            amt = float(input("Enter amount to deposit: "))
            b.deposit(amt)

            new_data = pd.DataFrame({
                "Date": [datetime.now()],
                "Credit/Debit": [amt],
                "Balance": [b.bal]
            })

            sheet_name = str(Accountno)

            old_data = pd.read_excel(file_name, sheet_name=sheet_name)

            updated_data = pd.concat([old_data, new_data], ignore_index=True)

            with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                updated_data.to_excel(writer, sheet_name=sheet_name, index=False)

        else:
            print("Create account first")



    # WITHDRAW
    elif n == 4:

        if b:

            amt = float(input("Enter amount to withdraw: "))
            b.withdraw(amt)

            new_data = pd.DataFrame({
                "Date": [datetime.now()],
                "Credit/Debit": [-amt],
                "Balance": [b.bal]
            })

            sheet_name = str(Accountno)

            old_data = pd.read_excel(file_name, sheet_name=sheet_name)

            updated_data = pd.concat([old_data, new_data], ignore_index=True)

            with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                updated_data.to_excel(writer, sheet_name=sheet_name, index=False)

        else:
            print("Create account first")



    # BALANCE WITH INTEREST
    elif n == 5:

        if b:
            b.bal_check()
        else:
            print("Create account first")



    # EXIT
    elif n == 6:

        print("Thank you for using bank portal")
        break


    else:
        print("Invalid choice")