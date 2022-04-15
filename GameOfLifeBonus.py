def outputAsHTML(matrix):
    filename = "output.html"
    with open(filename, 'w') as file:
        htmlPage = "<html><head><title>MATRIX</title></head><body>"

        htmlMatrix = "<div id=#matrix>"
        for line in matrix:
            htmlLine = ""
            for cell in line:
                htmlLine += str(cell)
            htmlMatrix += f"<div>{htmlLine}</div>"
        htmlMatrix += "</div>"

        htmlPage += htmlMatrix
        htmlPage += "</body></head></html>"

        file.write(htmlPage)


def FindNbNeighbors(xPos, yPos, gameCurrentState):
    if (xPos < 0 or yPos < 0 or xPos > len(gameCurrentState[0] or yPos > len(gameCurrentState))):
        return -1
    nbNeighbors = 0
    for i in range(3):
        if (yPos > 0 and xPos + i > 0 and xPos -1 + i < len(gameCurrentState[0]) and gameCurrentState[yPos-1][xPos-1+i]) != 0:
            nbNeighbors += 1
        if (yPos < len(gameCurrentState) - 1 and xPos + i > 0 and xPos -1 + i < len(gameCurrentState[0])  and gameCurrentState[yPos+1][xPos-1+i]) != 0:
            nbNeighbors += 1
    if (xPos > 0 and gameCurrentState[yPos][xPos-1]) != 0:
            nbNeighbors += 1
    if (xPos < len(gameCurrentState[0]) - 1 and gameCurrentState[yPos][xPos+1]) != 0:
            nbNeighbors += 1
    return nbNeighbors


def GameOfLife(nbTurns, initialState):
    
    gameState = initialState
    while (nbTurns > 0):
        nextGameState = []
        for y in range(len(gameState)):
            nextGameStateRow = []
            for x in range(len(gameState[y])):
                nbNeighbors = FindNbNeighbors(x, y, gameState)
                if (gameState[y][x]) == 1:
                    if (nbNeighbors <= 1) or (nbNeighbors >= 4):
                        nextGameStateRow.append(0)
                    else:
                        nextGameStateRow.append(1)
                else:
                    if (nbNeighbors == 3):
                        nextGameStateRow.append(1)
                    else:
                        nextGameStateRow.append(0)
            nextGameState.append(nextGameStateRow)
        nbTurns -= 1
        gameState = nextGameState
    outputAsHTML(gameState)
    return gameState


def ShowGameState(gameState):
    for y in gameState:
        for x in y:
            print(x, end="")
        print()


# Tests
# -----

# ShowGameState function.
'''
gameState = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
ShowGameState(gameState)
print("----------")


gameState = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
ShowGameState(gameState)
print("----------")


gameState = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]
ShowGameState(gameState)
print("----------")


gameState = [[1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,1,0], [1,0,0,0,1]]
ShowGameState(gameState)
print("----------")
'''
# ------------------------------------------------------------------------------

# FindNbNeighbors function.
'''
xPos = 0
yPos = 0
gameState = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]
print("The number of neighbors of the cell located at y:{} - x:{} is {}".format(yPos, xPos, FindNbNeighbors(xPos, yPos, gameState)))
print("--------------------")

xPos = 2
yPos = 2
gameState = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]
print("The number of neighbors of the cell located at y:{} - x:{} is {}".format(yPos, xPos, FindNbNeighbors(xPos, yPos, gameState)))
print("--------------------")

xPos = 4
yPos = 4
gameState = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]
print("The number of neighbors of the cell located at y:{} - x:{} is {}".format(yPos, xPos, FindNbNeighbors(xPos, yPos, gameState)))
print("--------------------")

xPos = 2
yPos = 0
gameState = [[1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,1,0], [1,0,0,0,1]]
print("The number of neighbors of the cell located at y:{} - x:{} is {}".format(yPos, xPos, FindNbNeighbors(xPos, yPos, gameState)))
print("--------------------")
'''

# ------------------------------------------------------------------------------

# GameOfLife function.

initialState = [[1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,1,0], [1,0,0,0,1]]
nbTurns = 5
print("INITIAL STATE :")
ShowGameState(initialState)
print("AFTER {} TURNS :".format(nbTurns))
finalState = GameOfLife(nbTurns, initialState)
ShowGameState(finalState)
print("----------")

# ------------------------------------------------------------------------------

'''
# outputAsHTML function.

matrix = [[1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,1,0], [1,0,0,0,1]]
outputAsHTML(matrix)
'''
