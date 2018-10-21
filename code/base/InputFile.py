name = input("Enter you name")

aFloat = float(input("enter a float"))

response = input("How many students are in your class: ")
print(int(response))

from urllib import request
response = request.urlopen(r'http://helloworldbook2.com/data/message.txt')
#response = request.urlopen(r'http://helloworldbook2.com/data/message.txt')
page = response.read()
page = page.decode('utf-8')
print(page)

