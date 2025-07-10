income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

savings = float(income) - float(expenses)

projected = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are ${int(savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected)}.")
