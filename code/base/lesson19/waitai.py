"""
AI Name: Wait AI

Made by: hzz

Strategy: Drive in wait.  Attack any robot in your front

"""


class AI:
    def __init__(self):
        self.turnTimes = 0

    def turn(self):
        if self.turnTimes == 0:
            self.robot.goForth()
            self.turnTimes = 1
            print(1)
        elif self.turnTimes == 1:
            self.robot.turnRight()
            self.turnTimes = 2
            print(2)
        elif self.turnTimes == 2:
            self.robot.turnRight()
            self.turnTimes = 3
            print(3)
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
            print(4)
        else:
            self.robot.doNothing()
            print(5)

