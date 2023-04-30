import budget
from budget import create_spend_chart
from unittest import main

# category 1
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and so on")
# category 2
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
# category 3
fun = budget.Category("Fun")
fun.deposit(1000, "initial deposit")
fun.withdraw(15)
# ...

# print invoices
print(food, "\n")
print(clothing, "\n")
print(fun, "\n")

# print the chart
print(create_spend_chart([food, clothing, fun]))
