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
    if input == '*':
        return True
    else:
        return False


def checkNeighbour(myRow, myIndex, origin):
    for i in range(myRow - 1, myRow + 2):
        if i < 0 or i >= len(inputs):
            continue
        for j in range(myIndex - 1, myIndex + 2):
            if j < 0 or j >= len(inputs[i]):
                continue
            if i == myRow and j == myIndex:
                continue
            if isSymbol(inputs[i][j]):
                if (i, j) in temp:
                    list = temp[(i, j)]
                    list[0] += 1
                    list.append(origin)
                    temp[(i, j)]= list
                else:
                    temp[(i, j)] = [1, origin]
                return True
    return False

inputs = []
sum = 0
i = 0
temp = {}

p = Path(__file__).with_name('inputs.txt')
with p.open("r") as file:
    for line in file:
        inputs.append([a for a in line])
with p.open("r") as file:
    for line in file:
        for match in re.finditer('\d+', line):
            for j in range(match.start(), match.end()):
                if checkNeighbour(i, j, int(match.group())):
                    break
        i += 1
for key in temp:
    list = temp[key]
    if list[0] == 2:
        sum += list[1] * list[2]
print(sum)
