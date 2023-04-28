class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
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


def create_spend_chart(categories):
    
    withdrawals = []
    names = []
    for category in categories:
        withdrawals.append(sum(item['amount'] for item in category.ledger if item['amount'] < 0))
        names.append(category.name)

    total = sum(withdrawals)
    percentages = [(withdrawal / total) * 100 for withdrawal in withdrawals]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        line = str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(name) for name in names)

    for i in range(max_name_length):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        chart += line
        if i < max_name_length - 1:
            chart += "\n"

    return chart
