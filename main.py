import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

fun = budget.Category("Fun")
fun.deposit(1000, "initial deposit")
fun.withdraw(15)

print(food, "\n")
print(clothing, "\n")
print(fun, "\n")

print(create_spend_chart([food, clothing, fun]))