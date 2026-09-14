print("Welcome to budget tracker")

total_budget = int(input("Please enter your initial budget"))

# ask question to user with 3 choices in a loop
# 1 add expense
#  - enter the description
#  - enter the amount
# print both
# 2 show details
#  - total budget
#  - expenses
#  - remaining budget
# 3 exit
#  - break the loop
expense_descripts = {}
exp_amts = []
while True:
    print("What would you like to do?")
    print("1. Add an Expense")
    print("2. Show budget details")
    print("3. Exit")
    choice = int(input("Enter your choice (1/2/3)?: "))
    if choice == 1:
        expense_descript = input("Enter expense descript")
        exp_amt = int(input("Enter expense amount"))
        exp_amts.append(exp_amt)
        expense_descripts[expense_descript] = exp_amt
        print(f"Added expense: {expense_descript}, Amount: {exp_amt}")
    elif choice == 2:
        print(f"Total Budget: {total_budget}")
        print(f"Expenses :")
        for expense_descript,exp_amt in expense_descripts.items():
            print(f" - {expense_descript}: {exp_amt}")
        print(f"Remaining Budget: {total_budget - sum(exp_amts)}")
    elif choice == 3:
        break
    else:
        print("Invalid Choice")