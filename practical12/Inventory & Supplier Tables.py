import pandas as pd

# Inventory Table
inventory = pd.DataFrame({
    "ITEM_ID": ["C101", "C102", "C103", "C104", "C105"],
    "ITEM_NAME": ["Denim Jeans", "Cotton Shirt", "Silk Saree", "Woolen Sweater", "Sports T-Shirt"],
    "CATEGORY": ["Bottomwear", "Topwear", "Ethnicwear", "Winterwear", "Active Wear"],
    "PRICE": [1500, 1200, 5000, 2000, 800],
    "STOCK": [30, 50, 20, 15, 60],
    "SUPPLIER": ["Levis", "Raymond", "Fabindia", "Spark", "Nike"]
})

# Supplier Table
supplier = pd.DataFrame({
    "SUPPLIER_ID": ["S201", "S202", "S203", "S204", "S205"],
    "SUPPLIER_NAME": ["Levis", "Raymond", "Fabindia", "Monte Carlo", "Nike"],
    "CONTACT": ["9876543210", "9123456789", "9988776655", "9345678123", "9234567890"],
    "LOCATION": ["Mumbai", "Delhi", "Bangalore", "Chandigarh", "Pune"]
})

# Merge tables
inv_data = pd.merge(inventory, supplier, left_on="SUPPLIER", right_on="SUPPLIER_NAME", how="left")

print("\nMerged Inventory Table:")
print(inv_data)

# Operations
print("\nAll items in inventory:")
print(inventory[["ITEM_NAME", "STOCK"]])

print("\nItems with stock > 20:")
print(inventory[inventory["STOCK"] > 20])

# Total value
inventory["TOTAL_VALUE"] = inventory["PRICE"] * inventory["STOCK"]
print("\nTotal Value of Items:")
print(inventory[["ITEM_NAME", "TOTAL_VALUE"]])