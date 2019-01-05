def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    return total


my_price = float(input("Enter a price: "))
# Call the function and store and print the result
totalPrice = calculate_tax(my_price, 0.06)
print("price = ", my_price, " Total price = ", totalPrice)
print(price)  # this line will cause an error