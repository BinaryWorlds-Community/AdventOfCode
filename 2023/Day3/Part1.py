from pathlib import Path
import re


def isInteger(input):
    try:
        i = int(input)
        return True
    except ValueError as ex:
        return False


def isDot(input):
    if input == '.':
        return True
    else:
        return False


def isEndOfLine(input):
    if input == '\n':
        return True
    else:
        return False


def isSymbol(input):
    if not (isEndOfLine(input) or isDot(input) or isInteger(input)):
        return True
    else:
        return False


def checkNeighbour(myRow, myIndex):
    for i in range(myRow - 1, myRow + 2):
        if i < 0 or i >= len(inputs):
            continue
        for j in range(myIndex - 1, myIndex + 2):
            if j < 0 or j >= len(inputs[i]):
                continue
            if isSymbol(inputs[i][j]):
                print(i + 1, j)
                return True
    return False


inputs = []
sum = 0
i = 0

p = Path(__file__).with_name('inputs.txt')
with p.open("r") as file:
    for line in file:
        inputs.append([a for a in line])
with p.open("r") as file:
    for line in file:
        for match in re.finditer('\d+', line):
            for j in range(match.start(), match.end()):
                if checkNeighbour(i, j):
                    print(i + 1, match.group(), match.start(), match.end())
                    sum += int(match.group())
                    break
        i += 1
print(sum)
