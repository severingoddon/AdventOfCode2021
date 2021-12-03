first, second, third, fourth, fifth = [], [], [], [], []
bits = [first, second, third, fourth, fifth]
allValues = []


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


def split(word):
    return [char for char in word]


def findNumbersWithHigherOccurence(fullList, index):
    currentBitList = bits[index]
    zeroCount = currentBitList.count("0")
    oneCount = bits[index].count("1")
    moreCommonBit = 0
    if zeroCount == oneCount:
        moreCommonBit = 1
    if zeroCount > oneCount:
        moreCommonBit = 0
    if zeroCount < oneCount:
        moreCommonBit = 1

    elementsToRemove = []
    if moreCommonBit == 1:
        for number in fullList:
            if number[index] == "0":
                elementsToRemove.append(number)
    if moreCommonBit == 0:
        for number in fullList:
            if number[index] == "1":
                elementsToRemove.append(number)
    newList = []
    for number in fullList:
        if not elementsToRemove.__contains__(number):
            newList.append(number)
    return newList


with open('input.txt') as file:
    for line in file:
        chars = split(line)
        if len(chars) > 5:
            chars.pop(len(chars) - 1)
        allValues.append(convert(chars))

        for i in range(len(chars)):
            bits[i].append(chars[i])

for i in range(len(bits)):
    if len(allValues) > 1:
        allValues = findNumbersWithHigherOccurence(allValues, i)

print(allValues)
