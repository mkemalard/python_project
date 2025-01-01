# SIMPLE SHOPPING CART PROGRAM
items = []
prices = []
total = 0

while True:
    item = input("Insert the item you buy (q or Q to quit): ")
    if item.lower() == "q":
        break 
    else:
        price = float(input(f"Enter the price of {item}: $"))
        items.append(item)
        prices.append(price)
print()    
print("======= Your Cart =======")

for item in items:
    print(f"{item:20} ${price}")

for price in prices:
    total += price

sum = "Your total is: "
print("-------------------------")
print(f"{sum:20} ${total}")
