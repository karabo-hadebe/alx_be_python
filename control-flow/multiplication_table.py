number = int(input("Enter a number to see its multiplication table: "))
times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in times:
    print(f"{number} * {times[n]} = {number*times[n]}")
