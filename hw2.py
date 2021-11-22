# Eren Demircan - 2237246
# CEng462 Artificial Intelligence - HW2
# UCS and A* with Graph Search Algorithm

# Explain the heuristic function and the reasoning behind it

# global variables, data structures

def moveLeft():
    # "LEFT"
    return


def moveUp():
    # "UP"
    return


def moveRight():
    # "RIGHT"
    return


def moveDown():
    # "DOWN"
    return


# heuristic function
def manhattanDistance():
    return


# read file into the variables and structures
def readProblem(fileName):
    return


# clear global variables and data structures
def clear():
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