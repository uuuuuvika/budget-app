import budget
from budget import create_spend_chart
from budget import Category
from unittest import main
import csv
from read_csv import load_csv 

# # category 1
# food = budget.Category("Food")
# food.deposit(1000, "Initial deposit")
# food.withdraw(10.15, "Groceries")
# food.withdraw(15.89, "Restaurant and so on")

# # category 2
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55, "Flea market")
# clothing.withdraw(100, "Zalando")

# # category 3
# fun = budget.Category("Fun")
# fun.deposit(100, "Initial deposit")
# fun.withdraw(35, "Berghain")
# # ...

# # print invoices
# print(food, "\n")
# print(clothing, "\n")
# print(fun, "\n")

# print the chart
# print(create_spend_chart([food, clothing, fun]))

# csv
# use comand line to update csv 
# click; check out others python library for sdding colors  


# categories = {}

# with open('transactions.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # skip header row
#     for row in reader:
#         category_name, transaction_type, amount, description = row
#         if category_name not in categories:
#             categories[category_name] = Category(category_name)
#         if transaction_type.upper() == 'DEP':
#             categories[category_name].deposit(float(amount), description)
#         elif transaction_type.upper() == 'WDRW':
#             categories[category_name].withdraw(float(amount), description)
#         elif transaction_type.upper() == 'TR':
#             if description not in categories:
#                 categories[description] = Category(description)
#             categories[category_name].transfer(float(amount), categories[description])

categories = load_csv()
print(categories)

for category in categories.values():
    print(category)