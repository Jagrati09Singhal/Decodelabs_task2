# Expense Tracker
# Developed by: Jagrati Singhal

print("=" * 40)
print("         EXPENSE TRACKER")
print("=" * 40)

expenses = []
total_spent = 0

num_expenses = int(input("Enter the number of expenses: "))

for i in range(num_expenses):
    expense = float(input(f"Enter expense {i + 1}: ₹"))
    expenses.append(expense)
    total_spent += expense

print("\n----- EXPENSE DETAILS -----")

for i in range(len(expenses)):
    print(f"Expense {i + 1}: ₹{expenses[i]}")

average_expense = total_spent / num_expenses

print("\n----- SUMMARY -----")
print("Total Expenses Entered :", num_expenses)
print("Total Amount Spent     : ₹", total_spent)
print("Average Expense        : ₹", round(average_expense, 2))
print("-------------------")

print("\nThank you for using Expense Tracker!")