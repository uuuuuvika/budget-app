from budget.create_spend_chart import create_spend_chart
from unittest import main
from load_csv import load_csv
import click

# TO DO:
# use comand line to update csv 
# click; check out others python library for sdding colors  

categories = load_csv()

for category in categories.values():
    print(category,  "\n")

print(create_spend_chart(categories.values()))