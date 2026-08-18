print("Tip Calculator")
t_bill = float(input("What was the total bill? $"))
t_percent = float(input("How much would you like to tip ? %")) / 100 + 1
t_people = int(input("How many people to split with? "))


t_total = round(t_bill*t_percent/t_people, 2)

print(f"Each person should pay: ${t_total:.2f}")