"""
AI Name: Wait AI

Made by: hzz

Strategy: Drive in wait.  Attack any robot in your front

"""


class AI:
    def __init__(self):
        self.turnTimes = 0
        self.shouldTurn = True

    def turn(self):
        if self.turnTimes == 0 and self.shouldTurn:
            self.robot.turnRight()
            self.turnTimes = 1
            self.shouldTurn = False
        elif self.turnTimes == 1 and self.shouldTurn:
            self.robot.turnRight()
            self.turnTimes = 2
        elif self.turnTimes == 2 and self.shouldTurn:
            self.robot.turnRight()
            self.turnTimes = 1
            self.shouldTurn = False
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
        elif self.robot.lookInFront() == "wall":
            self.shouldTurn = True
        else:
            self.robot.goForth()

