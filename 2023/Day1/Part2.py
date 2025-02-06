import re
from pathlib import Path

def getNumber(input):
    if input in lookupTable:
        return lookupTable.get(input)
    else:
        return int(input)

sum = 0
inputs = []
lookupTable = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
p = Path(__file__).with_name('inputs.txt')

with p.open("r") as file:
    for line in file:
        inputs.append(line)

for input in inputs:
    isolatedNumbers = list(re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))', input))
    first = getNumber(isolatedNumbers[0])
    last = getNumber(isolatedNumbers[-1])
    combined = 10 * first + last
    sum += combined
print(sum)
