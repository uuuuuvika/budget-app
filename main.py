import budget
from budget import create_spend_chart
from unittest import main

# category 1
food = budget.Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant and so on")
# category 2
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55, "Flea market")
clothing.withdraw(100, "Zalando")
# category 3
fun = budget.Category("Fun")
fun.deposit(100, "Initial deposit")
fun.withdraw(35, "Berghain")
# ...

# print invoices
print(food, "\n")
print(clothing, "\n")
print(fun, "\n")

# print the chart
print(create_spend_chart([food, clothing, fun]))

# csv
# use comand line to update csv 
# click; check out others python library for sdding colors  