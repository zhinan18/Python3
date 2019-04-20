import random

totals = [0, 0]
totals1 = ['1', '2']

for times in range(100000):
    result = random.choice(totals1)
    if result == totals1[0]:
        totals[0] += 1
    else:
        totals[0] = 0
    if totals[0] == 10:
        print(totals[0])
        totals[0] = 0
