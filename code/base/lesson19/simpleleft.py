# Listing 26-1
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# PythonBattle AI - first attempt to beat CircleAI

# Note that this is not a complete Python program itself,
#   it is a module called by the PythonBattle program.
# Save this as something like "betterthancircleai.py"
#   and try it in a battle against circleai.

class AI:
    def __init__(self):
        self.isFirstTurn = True

    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        elif self.isFirstTurn:
            self.robot.turnLeft()
            self.isFirstTurn = False
        elif self.robot.lookInFront() == "wall":
            self.robot.turnRight()
            self.currentlyDoing = "turnRight"
        else :
            self.robot.goForth()
