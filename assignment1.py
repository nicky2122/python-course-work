# 1. Product ID (int)
product_id = int(input("Enter Product ID: "))

# 2. Product Name (str)
product_name = "Samsung Mobile"  # given as example

# 3. Price (float)
price = float(input("Enter Product Price (in INR): "))

# 4. Categories (list)
categories_input = input("Enter categories (comma-separated): ")
categories = categories_input.split(",")  # creates a list

# 5. Stock Details (tuple) - (available, sold)
available_stock = int(input("Enter available stock: "))
sold_items = int(input("Enter sold items: "))
stock_details = (available_stock, sold_items)

# 6. Discount Percentage (float)
discount = float(input("Enter discount percentage: "))

# 7. Product Features (set)
features_input = input("Enter product features (comma-separated): ")
features = set(features_input.split(","))  # creates a set

# 8. Supplier Details (dict)
supplier_name = input("Enter supplier name: ")
supplier_contact = input("Enter supplier contact number: ")
supplier_location = input("Enter supplier location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

print("\nCollected Product Details:")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Categories: {categories}")
print(f"Stock Details (Available, Sold): {stock_details}")
print(f"Discount: {discount}%")
print(f"Features: {features}")
print(f"Supplier Info: {supplier_details}")
