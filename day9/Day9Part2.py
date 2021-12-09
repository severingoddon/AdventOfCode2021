height_map = []
lowPoints = [] # cointains points like [2, 4, 3] means 2 is the point, 4 is row and 3 is column
sum = []
basinSizes = []
alreadyVisitedPoints = []


def calculateBasin(i,j):
    checkNeigbours(i,j)
    sizeOfBasin = len(sum)+1
    sum.clear()
    return sizeOfBasin


def checkNeigbours(i,j):
    p = str(i)+str(j)
    if alreadyVisitedPoints.count(p) == 0:
        alreadyVisitedPoints.append(p)
        print("method called")
        if i == 0 and j == 0:  # upper left corner
            if height_map[i][j] < height_map[i + 1][j] != 9:
                newPoint = str(i+1)+str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i + 1, j)
            if height_map[i][j] < height_map[i][j + 1] != 9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)

        elif i == 0 and j == len(height_map[0]) - 1:  # upper right corner
            if height_map[i][j] < height_map[i + 1][j] != 9:
                newPoint = str(i + 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i+1, j)
            if height_map[i][j] < height_map[i][j - 1] != 9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)

        elif i == len(height_map) - 1 and j == 0:  # lower left corner
            if height_map[i][j] < height_map[i - 1][j] !=9:
                newPoint = str(i -1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)
            if height_map[i][j] < height_map[i][j + 1] !=9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)

        elif i == len(height_map) - 1 and j == len(height_map[0]) - 1:  # lower right corner
            if height_map[i][j] < height_map[i - 1][j] !=9:
                newPoint = str(i - 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)
            if height_map[i][j] < height_map[i][j - 1] !=9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)

        elif i == 0 and 0 < j < len(height_map[0]) - 1:  # upper row
            if height_map[i][j] < height_map[i + 1][j] !=9:
                newPoint = str(i + 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i+1,j)
            if height_map[i][j] < height_map[i][j + 1] !=9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)
            if height_map[i][j] < height_map[i][j - 1] !=9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)

        elif 0 < i < len(height_map) - 1 and j == 0:  # left column
            if height_map[i][j] < height_map[i + 1][j] != 9:
                newPoint = str(i + 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i+1,j)
            if  height_map[i][j] < height_map[i][j + 1] !=9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)
            if  height_map[i][j] < height_map[i - 1][j] != 9:
                newPoint = str(i - 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)

        elif 0 < i < len(height_map) - 1 and j == len(height_map[0]) - 1:  # right column
            if height_map[i][j] < height_map[i + 1][j] != 9:
                newPoint = str(i + 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i+1,j)
            if height_map[i][j] < height_map[i][j - 1] != 9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)
            if height_map[i][j] < height_map[i - 1][j] != 9:
                newPoint = str(i - 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)

        elif i == len(height_map) - 1 and 0 < j < len(height_map[0]) - 1:  # lower row
            if height_map[i][j] < height_map[i - 1][j] != 9:
                newPoint = str(i - 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)
            if height_map[i][j] < height_map[i][j - 1] != 9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)
            if height_map[i][j] < height_map[i][j + 1] != 9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)

        else:  # everything in the middle of the map
            if height_map[i][j] < height_map[i - 1][j] != 9:
                newPoint = str(i - 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i-1,j)
            if height_map[i][j] < height_map[i + 1][j] != 9:
                newPoint = str(i + 1) + str(j)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i+1,j)
            if height_map[i][j] < height_map[i][j + 1] != 9:
                newPoint = str(i) + str(j+1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j+1)
            if height_map[i][j] < height_map[i][j - 1] != 9:
                newPoint = str(i) + str(j-1)
                if alreadyVisitedPoints.count(newPoint) == 0: sum.append(1)
                checkNeigbours(i,j-1)



with open('input.txt') as file:
    for file_line in file:
        strippedLine = file_line.strip()
        newLine = []
        for number in strippedLine:
            newLine.append(int(number))
        height_map.append(newLine)



for i, row in enumerate(height_map):
    for j, column in enumerate(row):
        if i == 0 and j == 0:  # upper left corner
            if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]: lowPoints.append([i,j])
        elif i == 0 and j == len(height_map[0])-1: # upper right corner
            if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append([i,j])
        elif i == len(height_map)-1 and j == 0: # lower left corner
            if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]: lowPoints.append([i,j])
        elif i == len(height_map)-1 and j == len(height_map[0])-1: # lower right corner
            if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append([i,j])
        elif i == 0 and 0 < j < len(height_map[0])-1:  # upper row
            if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1] : lowPoints.append([i,j])
        elif 0 < i < len(height_map)-1 and j == 0:  # left column
            if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i-1][j]: lowPoints.append([i,j])
        elif 0 < i < len(height_map)-1 and j == len(height_map[0])-1:  # right column
            if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i-1][j]: lowPoints.append([i,j])
        elif i == len(height_map)-1 and 0 < j < len(height_map[0])-1:  # lower row
            if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i][j+1]: lowPoints.append([i,j])
        else:  # everything in the middle of the map
            if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i+1][j] and height_map[i][j] < height_map[i][j+1] and height_map[i][j] < height_map[i][j-1]: lowPoints.append([i,j])

for point in lowPoints:
    basinSizes.append(calculateBasin(point[0],point[1]))


sizes = sorted(basinSizes)
print(sizes[len(sizes)-1]*sizes[len(sizes)-2]*sizes[len(sizes)-3])

