def create_spend_chart(categories):
    
    withdrawals = []
    names = []
    for category in categories:
        withdrawals.append(sum(item['amount'] for item in category.invoice if item['amount'] < 0))
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