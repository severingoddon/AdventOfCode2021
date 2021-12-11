depthcount = 0
forwardcount = 0

with open('input.txt') as input:
    for line in input:
        splitted = line.split(" ")
        direction = splitted[0]
        value = int(splitted[1])
        if direction == 'forward':
            forwardcount += value
        if direction == 'down':
            depthcount += value
        if direction == 'up':
            depthcount -= value

print('result: ',depthcount*forwardcount)
