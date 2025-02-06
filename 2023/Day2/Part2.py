from pathlib import Path
import re

def getGameId(input):
    return int(re.findall('\d+', input)[0])

def getGameResult(input, gameId):
    splitted_games = input.split(";")
    isValid = True
    mGreen = 1
    mBlue = 1
    mRed = 1
    for game in splitted_games:
        green = 0
        blue = 0
        red = 0
        if re.search('\d+(?= green)',game) != None:
            green = int(re.search('\d+(?= green)',game)[0])
            if green > mGreen:
                mGreen = green
        if re.search('\d+(?= blue)', game) != None:
            blue = int(re.search('\d+(?= blue)',game)[0])
            if blue > mBlue:
                mBlue = blue
        if re.search('\d+(?= red)', game) != None:
            red = int(re.search('\d+(?= red)',game)[0])
            if red > mRed:
                mRed = red
        #if not (green <= max_cube_green and blue <= max_cube_blue and red <= max_cube_red):
         #   isValid = False
         #   break
    if isValid:
        minCubeProduct[gameId] = mGreen * mRed * mBlue
    return isValid


max_cube_blue = 14
max_cube_red = 12
max_cube_green = 13

inputs = []
validGameIds = []
minCubeProduct = {}
sum = 0
sumOfPowers = 0

p = Path(__file__).with_name('inputs.txt')
with p.open("r") as file:
    for line in file:
        gameId = getGameId(line.split(":")[0])
        gameResult = getGameResult(line.split(":")[1], gameId)
        if gameResult:
            validGameIds.append(gameId)
            sum += gameId
for key, value in minCubeProduct.items():
    print(f"{key} :  {value}")
    sumOfPowers += value
print(sumOfPowers)
