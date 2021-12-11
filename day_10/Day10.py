illegalCharacters, scores = [], []


def calculateScore(characters):
    score = 0
    for c in characters:
        score *= 5
        if c == ")": score += 1
        if c == "]": score += 2
        if c == "}": score += 3
        if c == ">": score += 4
    scores.append(score)


with open('input.txt') as file:
    for file_line in file:
        openList = []
        newline = file_line.strip()
        isCorrupted = False
        for c in newline:
            if c == "(": openList.insert(0, ")")
            if c == "[": openList.insert(0, "]")
            if c == "<": openList.insert(0, ">")
            if c == "{": openList.insert(0, "}")

            if c == ")":
                if openList[0] == ")": del openList[0]
                else:
                    illegalCharacters.append(c)
                    isCorrupted = True
                    break
            if c == "]":
                if openList[0] == "]": del openList[0]
                else:
                    illegalCharacters.append(c)
                    isCorrupted = True
                    break
            if c == ">":
                if openList[0] == ">": del openList[0]
                else:
                    illegalCharacters.append(c)
                    isCorrupted = True
                    break
            if c == "}":
                if openList[0] == "}": del openList[0]
                else:
                    illegalCharacters.append(c)
                    isCorrupted = True
                    break

        if not isCorrupted:
            calculateScore(openList)
        openList.clear()

print("Solution part 1 is: ",3 * illegalCharacters.count(")") + 57 * illegalCharacters.count("]") + 1197 * illegalCharacters.count("}") + 25137 * illegalCharacters.count(">"))
sorted_scores = sorted(scores)
print("Solution part 2 is: ",sorted_scores[int(len(scores)/2)])
