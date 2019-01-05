class HotDog:
    def __init__(self, level):
        self.cooked_level = 0
        self.cooked_string = "生的"
        self.condiments = []
        self.cook(level)

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "烤糊了的"
        elif self.cooked_level > 5:
            self.cooked_string = "做好了的"
        elif self.cooked_level > 3:
            self.cooked_string = "还没熟的"
        else:
            self.cooked_string = "生的"

    def add_condiment(self, condiment):
        self.condiments.append(condiment)
        # set the strings for the different cooked levels    # displays hot dog, including condiments

    def __str__(self):
        msg = "热狗"
        msg = self.cooked_string + msg
        return msg

myDog = HotDog(int(input("烤多久？")))  # create an instance
print(myDog)
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 more minutes...")
myDog.cook(3)
print(myDog)
print("What happens if I cook it for 10 more minutes?")
myDog.cook(10)
print(myDog)
print("Now, I'm going to add some stuff on my hot dog")
#myDog.add_condiment("胡椒")
#myDog.add_condiment("孜然")
print(myDog)