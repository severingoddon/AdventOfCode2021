import itertools
import collections

from day8.Pattern import Pattern
from day8.Numbers import MyNumbers

allPatterns = []


def createAllPatterns():
    permutations = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]))
    for p in permutations:
        pattern = Pattern(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
        allPatterns.append(pattern)


def findPattern(signals):
    for pattern in allPatterns:
        correctCount = 0
        for signal in signals:
            if checkSignalWithPattern(pattern, signal): correctCount += 1
        if correctCount > 9:
            return pattern


def checkSignalWithPattern(pattern, signal):
    letterArray = []
    for letter in signal:
        letterArray.append(pattern.getPositionOfLetter(letter))
    for l in allNumbers:
        if collections.Counter(l[0]) == collections.Counter(letterArray): return True
    return False


def decodeValues(pattern, values):
    number = ""
    for v in values:
        letterArray = []
        for letter in v:
            letterArray.append(pattern.getPositionOfLetter(letter))
        for l in allNumbers:
            if collections.Counter(l[0]) == collections.Counter(letterArray): number += l[1]
    return int(number)


allNumbers = MyNumbers.allNumbers
createAllPatterns()

with open('input.txt') as file:
    count = 0
    for i, file_line in enumerate(file):
        print("calculating line ", i, " of 200")
        splitted = file_line.split(" | ")
        signals = splitted[0].split()
        values = splitted[1].split()
        p = findPattern(signals)
        count += decodeValues(p, values)
print(count)
