# Lab 04 - Data Conversion Utility

print("==============================================")
print("          DATA CONVERSION UTILITY")
print("==============================================")

# Taking input from user
product_name = input("Enter Product Name: ")
price = input("Enter Price: ")
quantity = input("Enter Quantity: ")

# Type conversion
price = float(price)
quantity = int(quantity)

# Calculate total price
total_price = price * quantity

# Convert final amount to string
amount_str = str(total_price)

# Type Casting Summary
print("\n----------------------------------------------")
print("           TYPE CASTING SUMMARY")
print("----------------------------------------------")

print("Variable        Value          Python Type")

print("product_name   ", product_name, "       ", type(product_name))
print("price          ", price, "              ", type(price))
print("quantity       ", quantity, "           ", type(quantity))
print("total_price    ", total_price, "        ", type(total_price))
print("amount_str     ", amount_str, "         ", type(amount_str))

# Tax Invoice
print("\n==============================================")
print("                 TAX INVOICE")
print("==============================================")

print("Product Name   :", product_name)
print("Price per Unit : Rs.", price)
print("Quantity       :", quantity)
print("Invoice Total  : Rs.", total_price)

print("==============================================")