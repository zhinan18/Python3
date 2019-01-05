from lesson10 import my_module

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print("That's ", fahrenheit, " degrees Fahrenheit")
