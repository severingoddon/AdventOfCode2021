height_map = []
lowPoints = []
sum = 0


def findLowPoints():
    for i, row in enumerate(height_map):
        for j, column in enumerate(row):
            if i == 0 and j == 0:  # upper left corner
                if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]: lowPoints.append(height_map[i][j])
            elif i == 0 and j == len(height_map[0]) - 1:  # upper right corner
                if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append(height_map[i][j])
            elif i == len(height_map) - 1 and j == 0:  # lower left corner
                if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]: lowPoints.append(height_map[i][j])
            elif i == len(height_map) - 1 and j == len(height_map[0]) - 1:  # lower right corner
                if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append(height_map[i][j])
            elif i == 0 and 0 < j < len(height_map[0]) - 1:  # upper row
                if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append(height_map[i][j])
            elif 0 < i < len(height_map) - 1 and j == 0:  # left column
                if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i - 1][j]: lowPoints.append(height_map[i][j])
            elif 0 < i < len(height_map) - 1 and j == len(height_map[0]) - 1:  # right column
                if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j]: lowPoints.append(height_map[i][j])
            elif i == len(height_map) - 1 and 0 < j < len(height_map[0]) - 1:  # lower row
                if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i][j + 1]: lowPoints.append(height_map[i][j])
            else:  # everything in the middle of the map
                if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1]: lowPoints.append(height_map[i][j])
    return lowPoints


with open('input.txt') as file:
    for file_line in file: height_map.append(file_line.strip())
findLowPoints()

for p in lowPoints:
    sum += int(p)+1

print(sum)
