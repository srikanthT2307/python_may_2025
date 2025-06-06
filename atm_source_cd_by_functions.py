balance = 0

def menu_display():
    print("\n ATM menu:")
    print("1.Credit")
    print("2.Debit")
    print("3.Balance Enquiry")
    print("4.Exit")

def get_choice():
    return input(" enter the atm choice options(1-4): ")

def credit():
    global balance
    amount = int(input("enter the amount:  "))
    if  amount < 0:
        print("enter the postive correct amount")
    else: 
        balance += amount
        print(f"Rs {balance} credited to your savings account")

def debit():
    global balance
    amount = int(input("enter the amount:  "))
    if  amount < 0:
        print("enter the postive correct amount")
    elif amount > balance:
        print("Insufficient balance")
    else: 
        balance -= amount
        print(f"Rs {balance} debited from your savings account")

def Balance_Enquiry():
    print(f"Rs {balance} amount is the current balance")

def main_menu():
    while True:
        menu_display()
        choice = get_choice()
        if choice == "1":
            credit()
        elif choice == "2":
            debit()
        elif choice == "3":
            Balance_Enquiry()
        elif choice == "4":
            print("Thank you for chosing ATM services, Have a Good Day....!!!")
            break
        else:
            print("Thank you choose the right choice option")
main_menu()
