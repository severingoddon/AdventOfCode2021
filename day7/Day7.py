def findOptimumPos(part2):
    minimumFuelConsumption = sum(crabs) * 1000
    for pos in range(max(crabs)):
        consumption = 0
        for crab in crabs:
            difference = crab - pos
            if difference < 0: difference *= -1
            if part2:
                consumption += sum(range(difference + 1))
            else:
                consumption += difference
        if consumption < minimumFuelConsumption: minimumFuelConsumption = consumption
    print("Minimum consumption is: ", minimumFuelConsumption)


crabs = []

with open('input.txt') as file:
    for file_line in file:
        for x in file_line.split(","): crabs.append(int(x))
findOptimumPos(part2=False)
findOptimumPos(part2=True)
