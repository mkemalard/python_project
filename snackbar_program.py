menus = {"Nachos": 3.50,
        "Chips": 1.00,
        "Fries": 2.35,
        "Pretzel":4.55,
        "Pop corn": 6.00,
        "Soda": 1.50,
        "Milo": 1.50,
        "Lemonade": 4.25}
cart = {}
total = {}
grand_total = 0

print("====== MENU ======")
for menu, price in menus.items():
    print(f"{menu:10}: ${price:.2f}")
print("------------------")

while True:
    food = input("Select an item (Q to quit): ").capitalize()
    if food == "Q":
        break
    elif menus.get(food) is not None:
        qty = int(input("Enter Qty (q to quit): ")) 
        cart.update({food:qty})
        total_qty = qty * menus.get(food)
        total.update({food:(qty,total_qty)})
        grand_total += total_qty

print()
print("======== CART ========")
for food, (qty, total_qty) in total.items():
    print(f"{food:9} {qty:3} ${total_qty:> 7.2f}")

print("----------------------")
print(f"GRAND TOTAL:  $  {grand_total:.2f}")
