income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

Monthly_Savings = income - expenses

Annual_Savings = Monthly_Savings * 12  
Interest = (Annual_Savings * 0.05)
Projected_Savings = Annual_Savings + Interest

print("Your monthly savings are", Monthly_Savings)
print("Projected savings after one year, with interest, is:", Projected_Savings, ".")
