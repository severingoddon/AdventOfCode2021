octopusGrid = []
flashCount = 0
tester = 0

def doStep(flashCount):
    # increase all octopus energy levels
    for row in range(10):
        for column in range(10):
            octopusGrid[row][column] += 1

    alreadyFlashed = []
    # check all octopuses for flashing

    while True:
        print("tadaa")
        localCount = 0
        for row in range(10):
            for column in range(10):
                rowcolumn = str(row)+str(column)
                #test = octopusGrid[row][column]
                if octopusGrid[row][column] == 9 and alreadyFlashed.count(rowcolumn) == 0:
                    result = increase_or_flash(row, column, flashCount)
                    flashCount += result[0]
                    localCount += 1
                    for flashed in result[1]:
                        alreadyFlashed.append(flashed)
        if localCount == 0: break

    test = len(alreadyFlashed)
    alreadyFlashed.clear()
    return flashCount, test


def increase_or_flash(i,j, flashCount):
    alreadyFlashed = [str(i) + str(j)]
    octopusGrid[i][j] = 0
    flashCount += 1
    if i == 0 and j == 0:  # upper left corner
        if octopusGrid[i + 1][j] == 9:
            flashCount +=1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i+1) + str(j))
        if octopusGrid[i][j+1] == 9:
            flashCount +=1
            octopusGrid[i][j+1] = 0
            alreadyFlashed.append(str(i) + str(j+1))
        if octopusGrid[i+1][j+1] == 9:
            flashCount +=1
            octopusGrid[i+1][j+1] = 0
            alreadyFlashed.append(str(i+1) + str(j+1))

    elif i == 0 and j == len(octopusGrid[0]) - 1:  # upper right corner
        if octopusGrid[i + 1][j] == 9:
            flashCount += 1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i + 1) + str(j))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i + 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j - 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j - 1))

    elif i == len(octopusGrid) - 1 and j == 0:  # lower left corner
        if octopusGrid[i - 1][j] == 9:
            flashCount += 1
            octopusGrid[i - 1][j] = 0
            alreadyFlashed.append(str(i - 1) + str(j))
        if octopusGrid[i][j + 1] == 9:
            flashCount += 1
            octopusGrid[i][j + 1] = 0
            alreadyFlashed.append(str(i) + str(j + 1))
        if octopusGrid[i - 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j + 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j + 1))

    elif i == len(octopusGrid) - 1 and j == len(octopusGrid[0]) - 1:  # lower right corner
        if octopusGrid[i - 1][j] == 9:
            flashCount += 1
            octopusGrid[i - 1][j] = 0
            alreadyFlashed.append(str(i - 1) + str(j))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i - 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j - 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j - 1))

    elif i == 0 and 0 < j < len(octopusGrid[0]) - 1:  # upper row
        if octopusGrid[i + 1][j] == 9:
            flashCount += 1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i + 1) + str(j))
        if octopusGrid[i][j + 1] == 9:
            flashCount += 1
            octopusGrid[i][j + 1] = 0
            alreadyFlashed.append(str(i) + str(j + 1))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i + 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j - 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j - 1))
        if octopusGrid[i + 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j + 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j + 1))

    elif 0 < i < len(octopusGrid) - 1 and j == 0:  # left column
        if octopusGrid[i + 1][j] == 9:
            flashCount += 1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i + 1) + str(j))
        if octopusGrid[i-1][j] == 9:
            flashCount += 1
            octopusGrid[i-1][j] = 0
            alreadyFlashed.append(str(i-1) + str(j))
        if octopusGrid[i][j + 1] == 9:
            flashCount += 1
            octopusGrid[i][j + 1] = 0
            alreadyFlashed.append(str(i) + str(j + 1))
        if octopusGrid[i + 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j + 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j + 1))
        if octopusGrid[i - 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j + 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j + 1))

    elif 0 < i < len(octopusGrid) - 1 and j == len(octopusGrid[0]) - 1:  # right column
        if octopusGrid[i + 1][j] == 9:
            flashCount += 1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i + 1) + str(j))
        if octopusGrid[i-1][j] == 9:
            flashCount += 1
            octopusGrid[i-1][j] = 0
            alreadyFlashed.append(str(i-1) + str(j))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i + 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j - 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j - 1))
        if octopusGrid[i - 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j - 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j - 1))

    elif i == len(octopusGrid) - 1 and 0 < j < len(octopusGrid[0]) - 1:  # lower row
        if octopusGrid[i][j+1] == 9:
            flashCount += 1
            octopusGrid[i][j+1] = 0
            alreadyFlashed.append(str(i) + str(j+1))
        if octopusGrid[i-1][j] == 9:
            flashCount += 1
            octopusGrid[i-1][j] = 0
            alreadyFlashed.append(str(i-1) + str(j))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i - 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j - 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j - 1))
        if octopusGrid[i - 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j + 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j + 1))

    else:  # everything in the middle of the map
        if octopusGrid[i][j+1] == 9:
            flashCount += 1
            octopusGrid[i][j+1] = 0
            alreadyFlashed.append(str(i) + str(j+1))
        if octopusGrid[i-1][j] == 9:
            flashCount += 1
            octopusGrid[i-1][j] = 0
            alreadyFlashed.append(str(i-1) + str(j))
        if octopusGrid[i][j - 1] == 9:
            flashCount += 1
            octopusGrid[i][j - 1] = 0
            alreadyFlashed.append(str(i) + str(j - 1))
        if octopusGrid[i - 1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j - 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j - 1))
        if octopusGrid[i - 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i - 1][j + 1] = 0
            alreadyFlashed.append(str(i - 1) + str(j + 1))
        if octopusGrid[i+1][j - 1] == 9:
            flashCount += 1
            octopusGrid[i+1][j - 1] = 0
            alreadyFlashed.append(str(i+1) + str(j - 1))
        if octopusGrid[i + 1][j] == 9:
            flashCount += 1
            octopusGrid[i + 1][j] = 0
            alreadyFlashed.append(str(i + 1) + str(j))
        if octopusGrid[i + 1][j + 1] == 9:
            flashCount += 1
            octopusGrid[i + 1][j + 1] = 0
            alreadyFlashed.append(str(i + 1) + str(j + 1))
    return flashCount, alreadyFlashed


with open("inputFile.txt") as file:
    for file_line in file:
        grid_line = []
        for o in file_line.strip():
            grid_line.append(int(o))
        octopusGrid.append(grid_line)

print("size is: ", len(octopusGrid),"x",len(octopusGrid[0]))

for i in range(10):
    #flashCount += doStep(flashCount)
    tester += doStep(flashCount)[1]

print(tester)

