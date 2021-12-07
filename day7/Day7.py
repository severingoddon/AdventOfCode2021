import statistics


def findOptimumPos(part2, crabs):
    consumption = 0
    mean = int(statistics.mean(crabs))
    median = int(statistics.median(crabs))
    for crab in crabs:
        if part2: difference = crab - mean
        else: difference = crab - median
        if part2: consumption += sum(range(abs(difference) + 1))
        else: consumption += abs(difference)
    print(consumption)


with open('input.txt') as file:
    crabsArray = []
    for file_line in file:
        for x in file_line.split(","): crabsArray.append(int(x))
    findOptimumPos(part2=False, crabs=crabsArray)
    findOptimumPos(part2=True, crabs=crabsArray)
