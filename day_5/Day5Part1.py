lines = []
grid = []
pointsToMark = []


def buildGrid():
    highest_x_coordinate = 0
    highest_y_coordinate = 0
    for line in lines:
        for point in line:
            if int(point[0]) > highest_x_coordinate: highest_x_coordinate = int(point[0]) + 1
            if int(point[1]) > highest_y_coordinate: highest_y_coordinate = int(point[1]) + 1
    for x in range(highest_x_coordinate):
        gridline = []
        for y in range(highest_y_coordinate):
            gridline.append(".")
        grid.append(gridline)


def markLines():
    for line in lines:
        firstPoint = line[0]
        secondPoint = line[1]
        if firstPoint[0] == secondPoint[0]:  # x coordinates are the same
            y_difference = int(firstPoint[1]) - int(secondPoint[1])
            if y_difference > 0:
                for y in range(int(firstPoint[1]), int(secondPoint[1]) - 1, -1):
                    if grid[int(firstPoint[0])][y] == ".":
                        grid[int(firstPoint[0])][y] = 1
                    elif grid[int(firstPoint[0])][y] >= 1:
                        grid[int(firstPoint[0])][y] += 1
            else:
                for y in range(int(firstPoint[1]), int(secondPoint[1]) + 1):
                    if grid[int(firstPoint[0])][y] == ".":
                        grid[int(firstPoint[0])][y] = 1
                    elif grid[int(firstPoint[0])][y] >= 1:
                        grid[int(firstPoint[0])][y] += 1

        elif firstPoint[1] == secondPoint[1]:  # y coordinates are the same
            x_difference = int(firstPoint[0]) - int(secondPoint[0])
            if x_difference > 0:
                for x in range(int(firstPoint[0]), int(secondPoint[0]) - 1, -1):
                    if grid[x][int(firstPoint[1])] == ".":
                        grid[x][int(firstPoint[1])] = 1
                    elif grid[x][int(firstPoint[1])] >= 1:
                        grid[x][int(firstPoint[1])] += 1
            else:
                for x in range(int(firstPoint[0]), int(secondPoint[0]) + 1):
                    if grid[x][int(firstPoint[1])] == ".":
                        grid[x][int(firstPoint[1])] = 1
                    elif grid[x][int(firstPoint[1])] >= 1:
                        grid[x][int(firstPoint[1])] += 1


def countDangerousAreas():
    count = 0
    for line in grid:
        for point in line:
            if not point == ".":
                if point >= 2:
                    count += 1
    return count


with open('input.txt') as file:
    for line in file:
        splittedLine = line.split("->")
        firstPoint = splittedLine[0].split()
        secondPoint = splittedLine[1].split()
        firstPointCoordinates = firstPoint[0].split(",")  # [x , y]
        secondPointCoordinates = secondPoint[0].split(",")
        line = [firstPointCoordinates, secondPointCoordinates]
        if firstPointCoordinates[0] == secondPointCoordinates[0] or firstPointCoordinates[1] == secondPointCoordinates[1]:  # only consider vertical and horizontal lines
            lines.append(line)

buildGrid()
markLines()
print(countDangerousAreas())
