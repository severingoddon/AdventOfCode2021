import statistics


def findOptimumPos(part2, crabs):
    minimumFuelConsumption = sum(crabs) * 1000
    for pos in range(int(statistics.median(crabsArray)), max(crabs)):
        consumption = 0
        for crab in crabs:
            difference = crab - pos
            if difference < 0: difference *= -1
            if part2: consumption += sum(range(difference + 1))
            else: consumption += difference
        if consumption < minimumFuelConsumption:minimumFuelConsumption = consumption
        else: break
    print("Minimum consumption is: ", minimumFuelConsumption)


with open('input.txt') as file:
    crabsArray = []
    for file_line in file:
        for x in file_line.split(","): crabsArray.append(int(x))
    findOptimumPos(part2=False, crabs=crabsArray)
    findOptimumPos(part2=True, crabs=crabsArray)
