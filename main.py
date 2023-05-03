from budget import create_spend_chart
from unittest import main
import csv
from read_csv import load_csv 

# TO DO
# use comand line to update csv 
# click; check out others python library for sdding colors  

categories = load_csv()

for category in categories.values():
    print(category,  "\n")

print(create_spend_chart(categories.values()))