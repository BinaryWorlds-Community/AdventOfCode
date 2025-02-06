import re
from pathlib import Path

sum = 0
inputs = []
p = Path(__file__).with_name('inputs.txt')

with p.open("r") as file:
    for line in file:
        inputs.append(line)

for input in inputs:
    isolatedNumbers = list(map(int, re.findall('\d', input)))
    first = isolatedNumbers[0]
    last = isolatedNumbers[-1]
    combined = 10 * first + last
    sum += combined
print(sum)
