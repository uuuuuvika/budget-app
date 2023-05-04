import click

class Category:
    def __init__(self, name):
        self.name = name
        self.invoice = []

    def __str__(self):
        # ^ str should be centered
        title = click.style(f"{self.name:*^30}\n", fg="cyan")
        items = ""
        total = 0
        for item in self.invoice:
            # > str should be right-aligned
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        total_str = click.style(f"Total: {total}", fg="bright_cyan")
        output = title + items + total_str
        return output

    def deposit(self, amount, description=""):
        self.invoice.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.invoice.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.invoice:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
