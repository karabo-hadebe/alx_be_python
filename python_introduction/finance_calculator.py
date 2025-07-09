income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

Monthly_Savings = income - expenses

Annual_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print("Your monthly savings are", Monthly_Savings,"Projected savings after one year, with interest, is:", Annual_Savings, ".")
