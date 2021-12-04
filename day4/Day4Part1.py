import copy

numbers = ""
boards = []
count = 0
winnerBoard = None


def calculateScore(board):
    score = 0
    for numberLine in board:
        for number in numberLine:
            if number[1] == False:
                score = score + int(number[0])
    print('score is: ', score)


def markNumber(numberToMark):
    for board in boards:
        for numberLine in board:
            for number in numberLine:
                if number[0] == numberToMark:
                    number[1] = True


def checkBoards():
    for board in boards:
        if checkVertical(board):
            calculateScore(board)
            return True
        if checkHorizontal(board):
            calculateScore(board)
            return True
    return False


def checkVertical(board):
    for i in range(5):
        count = 0
        for numberLine in board:
            number = numberLine[i]
            if number[1]:
                count += 1
        if count == 5:
            return True
    count = 0
    return False


def checkHorizontal(board):
    for numberLine in board:
        count = 0
        for number in numberLine:
            if number[1]:
                count += 1
        if count == 5:
            return True
    count = 0
    return False


with open('input.txt') as file:
    board = []
    lineOfBoard = []
    for line in file:
        count += 1
        if len(line) > 16:
            numbers += line
        if len(line) == 1 and count > 5:
            boards.append(copy.deepcopy(board))
            board.clear()
        if 13 < len(line) < 16:
            boardNumbers = line.split()
            for char in boardNumbers:
                number = [char, False]
                lineOfBoard.append(number)
            board.append(copy.deepcopy(lineOfBoard))
            lineOfBoard.clear()
boards.append(board)

numbersWithoutComma = numbers.split(",")
for number in numbersWithoutComma:
    markNumber(number)
    if checkBoards():
        print(number)
        break


