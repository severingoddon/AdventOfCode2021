import time

depthcount, horizontalCount, aimcount = 0, 0, 0

with open('input.txt') as input:
    t1 = time.time_ns()
    for line in input:
        splitted = line.split(" ")
        direction = splitted[0]
        value = int(splitted[1])
        if direction == 'forward':
            horizontalCount += value
            depthcount += aimcount * value
        if direction == 'down':
            aimcount += value
        if direction == 'up':
            aimcount -= value

t2 = time.time_ns()

print('result: ', depthcount * horizontalCount)
print('time needed: ', (t2-t1))
