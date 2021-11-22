# Eren Demircan - 2237246
# CEng462 Artificial Intelligence - HW2
# UCS and A* with Graph Search Algorithm

# Explain the heuristic function and the reasoning behind it

# global variables, data structures
startState = []
targetState = []

####### 8-Puzzle Utilities Start #######
def moveLeft8(currentState):
    # "LEFT"
    x, y = findIndex(currentState, 0)
    if x > 0:
        temp = currentState[x][y - 1]
        currentState[x][y - 1] = 0
        currentState[x][y] = temp

    return


def moveUp8(currentState):
    # "UP"
    x, y = findIndex(currentState, 0)
    if y > 0:
        temp = currentState[x - 1][y]
        currentState[x - 1][y] = 0
        currentState[x][y] = temp

    return


def moveRight8(currentState):
    # "RIGHT"
    x, y = findIndex(currentState, 0)
    if x < 2:
        temp = currentState[x][y + 1]
        currentState[x][y + 1] = 0
        currentState[x][y] = temp

    return


def moveDown8(currentState):
    # "DOWN"
    x, y = findIndex(currentState, 0)
    if y < 2:
        temp = currentState[x + 1][y]
        currentState[x + 1][y] = 0
        currentState[x][y] = temp

    return


# heuristic function
def manhattanDistance():

    heuristicEval = 0

    for i in range(0, 8):
        x1, y1 = findIndex(startState, i)
        x2, y2 = findIndex(targetState, i)

        distance = abs(x2 - x1) + abs(y2- y1)
        heuristicEval += distance

    return heuristicEval


def findIndex(arr, val):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == val:
                return i, j


def convertState(state):
    
    res = ""
    for row in state:
        for col in row:
            if col == 0:
                res += ' '
            else:
                res += str(col)
    
    return res

# read file into the variables and structures
def readProblem(fileName):

    lines = []

    with open(fileName, 'r') as f:
        lines.append(f.readline()[:-1])
        lines.append(f.readline()[:-1])
        lines.append(f.readline()[:-1])
        f.readline()
        lines.append(f.readline()[:-1])
        lines.append(f.readline()[:-1])
        lines.append(f.readline())

    for line in lines:
        if len(startState) < 3:
            result = line.split(' ')
            row = [int(result[0]), int(result[1]), int(result[2])]
            startState.append(row)
        elif len(targetState) < 3:
            result = line.split(' ')
            row = [int(result[0]), int(result[1]), int(result[2])]
            targetState.append(row)

    return


# clear global variables and data structures
def clear():
    startState = []
    targetState = []
    return

def InformedSearch(methodName, fileName):

    if methodName == "UCS":
        clear()
        readProblem(fileName)
        UCS()
        return

    elif methodName == "AStar":
        clear()
        readProblem(fileName)
        AStar()
        return

    else:
        print("Unknown search method")
    
    return


# Uniform-Cost Search
def UCS():
    return


# A* search
def AStar():
    return

def printArr(state):
    for row in state:
        print(row)
    
    return

readProblem("eightpuzzle1.txt")
print(manhattanDistance())