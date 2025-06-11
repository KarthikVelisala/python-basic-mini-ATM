menu = {
    "Pizza": 150,
    "Burger": 100,
    "Cool drink": 20,
    "Salad": 120,
    "Coffee": 50,
    "Pasta": 80,
}

import time

print("Welcome to our restaurant")
time.sleep(2)

print("\nHere's your menu, sir:")
for item, price in menu.items():
    print(f" {item} : Rs {price}")

order_total = 0
order_items = []

while True:
    item = input("\nEnter the name of the item you want to order: ").strip().title()  # Fixed case
    if item in menu:
        order_total += menu[item]
        order_items.append(item)
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry sir your '{item}' is not available on the menu.")

    another = input("Would you like to order anything else? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Final order summary
if order_items:
    print("\nOrder summary:")
    for item in order_items:
        print(f" - {item} : Rs {menu[item]}")
    print(f"Total amount to pay: Rs {order_total}")
else:
    print("\nNo valid items were ordered.")
