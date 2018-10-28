
print("Type 3 to continue, anything else to quit.")
someInput = input()

# Keep looping as long as someInput ='3'
while someInput == '3':
    print("Thank you for the 3.  Very kind of you.")
    print("Type 3 to continue, anything else to quit.")    # Body of the loop
    someInput = input()                               #
print("That's not 3, so I'm quitting now.")


for i in range (1, 6):
    print
    print('i =', i,)
    print('Hello, how',)
    if i == 3:
        continue
    print('are you today?')


