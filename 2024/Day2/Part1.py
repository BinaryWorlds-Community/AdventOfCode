from pathlib import Path
import re


def is_safe(levels) -> bool:
    is_safe: bool = False
    direction: int = 0
    for entry in range(len(levels)-1):
        if(not is_valid_distance(levels[entry], levels[entry+1])):
            
            return is_safe
        if(entry == 0):
            direction = get_direction(levels[entry], levels[entry+1])
        elif(not direction == get_direction(levels[entry], levels[entry+1])):
            return is_safe
    is_safe = True
    return is_safe

def get_direction(valA: int, valB: int):
    if valA > valB:
        return -1
    elif valA < valB:
        return 1
    return 0

def is_valid_distance(valA: int, valB: int) -> bool:
    if(distance(valA,valB) >= 1 and distance(valA,valB) <= 3):
        return True
    return False

def distance(valA:int, valB:int) -> int:
    return abs(valA - valB)

p = Path(__file__).with_name('input.txt')
safe_counter: int = 0
reports = []

with p.open("r") as file:
    for report in file:
        reports.append(report)
for report in reports:
    levels = list(map(int, re.findall(r'[0-9]+', report)))
    #print(f"{levels} {len(levels)}")
    if(is_safe(levels)):
        safe_counter += 1

print(safe_counter)
