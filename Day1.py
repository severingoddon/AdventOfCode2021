previousMeasurement = 0
timesIncreased = 0

with open('Day1Input1.txt') as input:
    for line in input:
        if previousMeasurement != 0:
            if int(line) > previousMeasurement:
                timesIncreased += 1
        previousMeasurement = int(line)

print('result challenge 1: ', timesIncreased)

previousSum = 0
timesIncreased2 = 0

with open('Day1Input1.txt') as input:
    lines = input.readlines()
    for i in range(len(lines) - 1):
        if 0 < i < len(lines):
            sum = int(lines[i - 1]) + int(lines[i]) + int(lines[i + 1])
            if sum > previousSum != 0:
                timesIncreased2 += 1
            previousSum = sum

print('result challenge 2: ', timesIncreased2)
