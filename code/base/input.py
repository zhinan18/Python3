somebody = ""
print("Enter your name:")

somebody = raw_input()
print( "Hi", somebody, "how are you today?")

temp_string = input()
fahrenheit = float(temp_string)
print(fahrenheit)

import urllib2
file = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
message = file.read()
print(message)
