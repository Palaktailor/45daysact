wallet = 0.0
expenses = []
 # add income
income = int(input("your income:"))
wallet += income 
print("after income added:",wallet)

num_expenses = int(input("how many expenses you want to add:"))

for i in range(num_expenses):
    name = input(f"Enter your expenses = {i+1}: " )
    amount = int(input(f"enter your amount for {name}: "))
    expenses.append({"name":name, "amount":amount})
    wallet -= amount
    # print(expenses)
    for e in expenses:
        print(f"{e["name"]},{e["amount"]}")
print("after expenses:",wallet)

saving_percentage = int(input("how much saving percentange "))
save = income*saving_percentage/100
wallet  -=save
print("after savings",wallet)

print("total amount left in wallet ",wallet)

