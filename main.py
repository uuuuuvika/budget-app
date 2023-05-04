from budget.create_spend_chart import create_spend_chart
from unittest import main
from load_csv import load_csv
import click

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def my_program(file_path):
    categories = load_csv(file_path)
    for category in categories.values():
        print(category,  "\n")
    print(create_spend_chart(categories.values()))

if __name__ == '__main__':
    my_program()


# TO DO: update CSV from CL