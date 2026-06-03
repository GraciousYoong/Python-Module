#!/usr/bin/env python3

import sys


print("=== Inventory System Analysis ===")

inventory: dict[str, int] = {}
seen_items: list[str] = []


index = 1
while index < len(sys.argv):
    arg = sys.argv[index]

    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        index += 1
        continue

    parts = arg.split(":")

    if len(parts) != 2:
        print(f"Error - invalid parameter '{arg}'")
        index += 1
        continue

    item = parts[0]
    qty_str = parts[1]

    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
        index += 1
        continue

    try:
        qty = int(qty_str)
    except ValueError as error:
        print(
            f"Quantity error for '{item}': {error}"
        )
        index += 1
        continue

    inventory.update({item: qty})
    seen_items.append(item)

    index += 1


print(f"Got inventory: {inventory}")

item_list = list(inventory.keys())
print(f"Item list: {item_list}")

total_quantity = sum(inventory.values())
print(
    f"Total quantity of the {len(inventory)} items: "
    f"{total_quantity}"
)

for item in inventory.keys():
    percent = round((inventory[item] / total_quantity) * 100, 1)
    print(f"Item {item} represents {percent}%")

max_qty = max(inventory.values())
min_qty = min(inventory.values())

most_item: str = ""
least_item: str = ""

for item in seen_items:
    if inventory[item] == max_qty and most_item == "":
        most_item = item
    if inventory[item] == min_qty and least_item == "":
        least_item = item

print(
    f"Item most abundant: {most_item} with quantity {inventory[most_item]}"
)
print(
    f"Item least abundant: {least_item} with quantity {inventory[least_item]}"
)
