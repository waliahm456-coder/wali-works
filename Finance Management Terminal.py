import time as tm
import matplotlib.pyplot as plt
# from flask import Flask, render_template, request, redirect

#initialisations
balance = 1000
ID_counter = 1
records = []

#modules
#show balance
def show_balance():
    print("------")
    print("Balance = ", balance)
    print("------")
    print("\n")
    tm.sleep(2)

#main menu display
def main_menu():
    print("Welcome to Financo! : YOUR FINANCE PATNER")
    print("\n")
    print("Choose the option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. View")
    print("4. Design")
    print("5. Exit")
    print("\n")

#error wait
def wait():
    print("\n")
    tm.sleep(2)

#validate the amount entered by user
def validate_amount():
        global amount
        while True:
            print("\n")
            amount = input("Enter amount to withdraw (Whole number): ")
            try:
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Enter a positive Value")
                    wait()

            except ValueError:
                print("Please enter a valid whole number.")
                wait()

# #ui stuff Flask
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("index.html", records=records)

# app.run(debug=True)

#table
class Transactions():
    def __init__(self, ID, Type, Amount, Reason):
        self.ID = ID
        self.Type = Type
        self.Amount = Amount
        self.Reason = Reason

    def __str__(self):
        return f"ID: {self.ID} | Type: {self.Type} | Amount: {self.Amount} | Reason: {self.Reason}"


while True:
    main_menu()

    #choice validation
    while True:
        choice = str(input("Enter choice (1--4): "))
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            break
        else:
            print("Invalid choice!!!")
            wait()

    #withdraw
    if choice == "1":
        validate_amount()

        #If user tries to withdraw more than balance
        if amount > balance:
            print("ERROR: Insufficent balance!")
            wait()

        else:
            reason = input("Enter Reason for this transaction (Optional): ")
            balance = balance - amount

            #input in records
            this_record = Transactions(ID_counter, "Out", amount, reason)
            records.append(this_record)
            ID_counter = ID_counter+1

            print("TRANSACTION COMPLETED")
            wait()
            show_balance()

    
    #deposit
    if choice == "2":
        validate_amount()

        reason = input("Enter Reason for this transaction (Optional): ")
        balance = balance + amount        

        this_record = Transactions(ID_counter, "In", amount, reason)
        records.append(this_record)
        ID_counter = ID_counter+1

        print("TRANSACTION COMPLETED")
        wait()
        show_balance()

    #view
    if choice == "3":
        print("TRANSACTIONS HISTORY")
        for record in records:
            print(record)

        print("\n")
        wait()

        

        #expenses vs spending graph
        print("INCOME VS EXPENSES")

        income = 0
        for record in records:
            if record.Type == "In":
                income = income + record.Amount

        expense = 0
        for record in records:
            if record.Type == "Out":
                expense = expense + record.Amount

        Amounts_for_graph = [income, expense]
        x_axis = ["INCOME", "EXPENSES"]

        plt.bar(x_axis, Amounts_for_graph, color=["blue", "red"])
        plt.title("INCOME VS EXPENSES")
        plt.ylabel("AMOUNT")
        plt.show()