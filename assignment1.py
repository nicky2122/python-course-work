# Zee5 Product Details (Direct Data Assignment)

# 1. Product ID and Name
product_id = 2002
product_name = "Zee5 Premium Subscription"

# 2. Price
price = 999.0

# 3. Categories as list
categories = ["Subscription", "OTT", "HD Content"]

# 4. Stock details as tuple (available licenses, used licenses)
stock_details = (1000, 760)

# 5. Discount percentage
discount = 15.0

# 6. Product features as set
product_features = {"4K Streaming", "Ad-Free", "Multi-device"}

# 7. Supplier details as dictionary
supplier_details = {
    "name": "Zee5 Digital Media",
    "contact": "support@zee5.com",
    "location": "Mumbai"
}

# 8. Discounted price calculation
discounted_price = price - (price * discount / 100)

# 🧾 Display Zee5 Product Summary
print("----- 🎬 Zee5 Product Summary -----")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Discount: {discount:.1f}%")
print(f"Discounted Price: ₹{discounted_price:.2f}")
print(f"Categories: {', '.join(categories)}")
print(f"Stock (Available/Used): {stock_details[0]}/{stock_details[1]}")
print(f"Features: {', '.join(product_features)}")
print(f"Supplier: {supplier_details['name']}")
print(f"Contact: {supplier_details['contact']}")
print(f"Location: {supplier_details['location']}")
