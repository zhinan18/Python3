from math import pi


left = 'x**2'
right = '2'
realx = None


def solve(x,accuracy):
    global left, right, realx
    bestx = x
    x -= accuracy*6
    print('startingx:', x)
    print('accuracy:', accuracy)
    #gives the smallest difference a value
    try:
        smallest = eval(left)-eval(right)
    except:
        print('error found when giving "smallest" a value!x was', x)
        x += accuracy/10
        smallest = eval(left)-eval(right)
        smallest = abs(round(smallest, 12))
    for i in range(-1,11):
        x += accuracy
        x = round(x,12)
        #tries to find the difference and avoid any error
        try:
            difference = eval(left)-eval(right)
        except:
            print('error found when calculating difference! x was', x)
            x += accuracy/10
            difference = eval(left)-eval(right)
            difference = abs(round(difference, 12))
            #reaction to different differences
        if difference == 0:
            print('yeah')
            print(x)
            print('difference', difference)
            realx = x
            return 0
        elif difference < smallest:
            smallest = difference
            bestx = x
            #checks if the value is accurate enough
    if accuracy < 0.000001:
        print('yipee')
        print(bestx)
        realx = x
        return 0
    print('endingx', x)
    print('currentx', bestx)
    print('smallest', smallest)
    print("-------------------------")
    solve(bestx, accuracy/10)
solve(0, 1000000)
print(realx)
realx = round(realx, 9)
print(realx)
