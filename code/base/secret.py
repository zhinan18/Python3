import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print ("AHOY!  I'm the Dm,.read Pirate Roberts, and I have a secret!")
print ("It is a number from 1 to 99.  I'll give you 6 tries. ")
while guess != secret and tries < 6:
    try:
        guess = input("What's yer guess? ")

        if int(guess) < secret:
            print ("Too low, ye scurvy dog!")
        elif int(guess) > secret:
            print ("Too high, landlubber!")
        tries = tries + 1
        print("There are ",6-tries," other opportunities leftchances")
    except ValueError:
        print("please input digit!!")
if guess == secret:
    print ("Avast! Ye got it!  Found my secret, ye did!")
else:
    print ("No more guesses!  Better luck next time, matey!")
    print ("The secret number was", secret)
