from pathlib import Path
import re


def getGameId(input):
    return int(re.findall('\d+', input)[0])


def getGameResult(input):
    splitted_games = input.split(";")
    isValid = True
    for game in splitted_games:
        green = 0
        blue = 0
        red = 0
        if re.search('\d+(?= green)', game) != None:
            green = int(re.search('\d+(?= green)', game)[0])
        if re.search('\d+(?= blue)', game) != None:
            blue = int(re.search('\d+(?= blue)', game)[0])
        if re.search('\d+(?= red)', game) != None:
            red = int(re.search('\d+(?= red)', game)[0])
        if not (green <= max_cube_green and blue <= max_cube_blue and red <= max_cube_red):
            isValid = False
            break
    return isValid


max_cube_blue = 14
max_cube_red = 12
max_cube_green = 13

inputs = []
validGameIds = []
sum = 0

p = Path(__file__).with_name('inputs.txt')
with p.open("r") as file:
    for line in file:
        gameId = getGameId(line.split(":")[0])
        gameResult = getGameResult(line.split(":")[1])
        if gameResult:
            validGameIds.append(gameId)
            sum += gameId
print(sum)
