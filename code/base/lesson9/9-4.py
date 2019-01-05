def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    my_price = 1
    print(my_price)
    return total


my_price = float(input("Enter a price: "))
totalPrice = calculate_tax(my_price, 0.06)
print("price = ", my_price, " Total price = ", totalPrice)
