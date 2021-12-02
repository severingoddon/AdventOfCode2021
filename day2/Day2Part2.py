depthcount = 0
horizontalCount = 0
aimcount = 0

with open('input.txt') as input:
    for line in input:
        splitted = line.split(" ")
        direction = splitted[0]
        value = int(splitted[1])
        if direction == 'forward':
            horizontalCount += value
            depthcount += aimcount*value
        if direction == 'down':
            aimcount += value
        if direction == 'up':
            aimcount -= value

print('result: ',depthcount*horizontalCount)
