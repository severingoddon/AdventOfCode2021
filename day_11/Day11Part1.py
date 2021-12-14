from day_11.Squid import Squid
import copy
squidGrid = []
allSquids = []
stepcount = 0


def doStep(stepcount):
    for squid in allSquids: squid.check()
    for squid in allSquids:
        if not squid.hasFlashed: squid.increaseCount()
    checkIfAllFlashed(stepcount)
    for squid in allSquids: squid.hasFlashed = False


def checkIfAllFlashed(stepcount):
    if stepcount == 100:
        print("Count of all octopus flashes after 100 steps: ", calculateSumOfFlashes())  # solution of part 1
    flashCount = 0
    for squid in allSquids:
        if squid.hasFlashed: flashCount += 1
    if flashCount == len(allSquids):
        print("First step where all octopuses flashed at the same time ",stepcount) # solution of part 2
        quit(0)


def calculateSumOfFlashes():
    sum_of_flashes = 0
    for squid in allSquids:
        sum_of_flashes += squid.total_flash_count
    return sum_of_flashes


def setNeighbours(squid):
    name = squid.name
    i, j = int(name[0]), int(name[1])
    for s in allSquids:
        if i == 0 and j == 0:  # upper left corner
            if s.name == str(i+1)+str(j): squid.neighbours.append(s)
            elif s.name == str(i)+str(j+1): squid.neighbours.append(s)
            elif s.name == str(i+1) + str(j + 1): squid.neighbours.append(s)

        elif i == 0 and j == len(squidGrid[0]) - 1:  # upper right corner
            if s.name == str(i + 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j - 1): squid.neighbours.append(s)

        elif i == len(squidGrid) - 1 and j == 0:  # lower left corner
            if s.name == str(i-1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j + 1): squid.neighbours.append(s)

        elif i == len(squidGrid) - 1 and j == len(squidGrid[0]) - 1:  # lower right corner
            if s.name == str(i - 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j - 1): squid.neighbours.append(s)

        elif i == 0 and 0 < j < len(squidGrid[0]) - 1:  # upper row
            if s.name == str(i+1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j + 1): squid.neighbours.append(s)

        elif 0 < i < len(squidGrid) - 1 and j == 0:  # left column
            if s.name == str(i + 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j + 1): squid.neighbours.append(s)

        elif 0 < i < len(squidGrid) - 1 and j == len(squidGrid[0]) - 1:  # right column
            if s.name == str(i + 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j - 1): squid.neighbours.append(s)

        elif i == len(squidGrid) - 1 and 0 < j < len(squidGrid[0]) - 1:  # lower row
            if s.name == str(i) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j + 1): squid.neighbours.append(s)

        else:  # everything in the middle of the map
            if s.name == str(i) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i - 1) + str(j + 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j - 1): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j): squid.neighbours.append(s)
            elif s.name == str(i + 1) + str(j + 1): squid.neighbours.append(s)
    return squid


with open("inputFile.txt") as file:
    for file_line in file:
        grid_line = []
        for o in file_line.strip():
            grid_line.append(int(o))
        squidGrid.append(copy.deepcopy(grid_line))
        grid_line.clear()

for i in range(10):
    for j in range(10):
        squid = Squid(int(squidGrid[i][j]), False, str(i)+str(j))
        allSquids.append(squid)

for squid in allSquids:
    squid = setNeighbours(squid)

# --------------------------------finished data preparation-----------------------------------

while True:
    stepcount += 1
    doStep(stepcount)



