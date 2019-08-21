"""
AI Name: yStraight AI

Made by: Carter

Strategy: Drive in circles.  Attack any robot in your path.

"""


class AI:
    def __init__(self):
        self.turnTimes = 0
        self.moveTimes = 0
        self.isForth = True

    def turn(self):
        if self.isForth:
            self.robot.goForth()
            self.turnTimes = self.turnTimes + 2
            self.isForth = False
        elif self.turnTimes > 0:
            self.robot.turnLeft()
            self.turnTimes -= 1
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
            self.turnTimes += 2
            self.moveTimes += 7
        elif self.moveTimes > 0:
            self.robot.goForth()
            self.moveTimes -= 1
        else:
            self.robot.doNothing()
