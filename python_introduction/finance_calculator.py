income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses

psavings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are", savings,"Projected savings after one year, with interest, is:", ps, ".")
