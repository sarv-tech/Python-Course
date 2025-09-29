# Q. Given a dictionary of products and their prices, find the product with the highest price.



my_products = {"watch": "$500", "wallet": "$400", "i pad": "$900"}
print(my_products)

# Convert price values to integers for comparison
prices = {product: int(price.strip("$")) for product, price in my_products.items()}

# Find the product with the highest price
highest_product = max(prices, key=prices.get)
highest_price = my_products[highest_product]  # keep the original "$" format

print("Product with highest price:", highest_product)
print("Price:", highest_price)
