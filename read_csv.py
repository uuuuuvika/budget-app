import csv
from budget import Category

def load_csv():
    categories = {}
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # to skip header row
        for row in reader:
            category_name, transaction_type, amount, description = row
            if category_name not in categories:
                categories[category_name] = Category(category_name)
            if transaction_type.upper() == 'DEP':
                categories[category_name].deposit(float(amount), description)
            elif transaction_type.upper() == 'WDRW':
                categories[category_name].withdraw(float(amount), description)
            elif transaction_type.upper() == 'TR':
                if description not in categories:
                    categories[description] = Category(description)
                categories[category_name].transfer(float(amount), categories[description])
    return categories


