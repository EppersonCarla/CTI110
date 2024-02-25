# Carla Epperson

# 02/25/2024

# P1HW2

# Basic math program

budget = float(input("Enter your total budget: $"))
destination = input("Enter your travel destination: ")
gas_expense = float(input("Enter the amount you will spend on gas: $"))
accommodation_expense = float(input("Enter the amount you will spend on your accommodation or hotel: $"))
food_expense = float(input("Enter the amount you will spend on food: $"))
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses
print("\nBudget: $", budget)
print("Travel Destination:", destination)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)

'''
1. Get user's budget.
2. Get user's travel destination.
3. Get user's gas expense.
4. Get user's accommodation expense.
5. Get user's food expense.
6. Calculate total expenses.
7. Calculate remaining budget.
8. Display budget, destination, total expenses, and remaining budget to the user.

'''



