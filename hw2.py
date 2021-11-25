# Eren Demircan - 2237246
# CEng462 Artificial Intelligence - HW2
# UCS and A* with Graph Search Algorithm

# Explain the heuristic function and the reasoning behind it

# global variables, data structures
startState = []
targetState = []

startPos = []
targetPos = [] 
currentPos = []

maze = []
mazeWidth = -1
mazeHeight = -1

path = []
eightPuzzle = True

class Node:
    def __init__(self, state, parent, cost):
        # current state of the puzzle
        self.state = state
        self.parent = parent
        self.cost = cost


def copy(arr):
    result = [ [ 0 for x in range(len(arr[0]))] for y in range(len(arr))]

    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            result[i][j] = arr[i][j]

    return result

####### 8-Puzzle Utilities Start #######
def moveLeft8(currentNode):
    # "LEFT"
    tempNode = Node(None, currentNode, currentNode.cost + 1)
    tempNode.state = copy(currentNode.state)
    
    x, y = findIndex(tempNode.state, 0)
    if y > 0:
        temp = tempNode.state[x][y - 1]
        tempNode.state[x][y - 1] = 0
        tempNode.state[x][y] = temp
        return tempNode
    else:
        return None


def moveUp8(currentNode):
    # "UP"
    tempNode = Node(None, currentNode, currentNode.cost + 1)
    tempNode.state = copy(currentNode.state)
    
    x, y = findIndex(tempNode.state, 0)
    if x > 0:
        temp = tempNode.state[x - 1][y]
        tempNode.state[x - 1][y] = 0
        tempNode.state[x][y] = temp
        return tempNode
    else:
        return None


def moveRight8(currentNode):
    # "RIGHT"
    tempNode = Node(None, currentNode, currentNode.cost + 1)
    tempNode.state = copy(currentNode.state)
    
    x, y = findIndex(tempNode.state, 0)
    if y < 2:
        temp = tempNode.state[x][y + 1]
        tempNode.state[x][y + 1] = 0
        tempNode.state[x][y] = temp
        return tempNode
    else:
        return None


def moveDown8(currentNode):
    # "DOWN"
    tempNode = Node(None, currentNode, currentNode.cost + 1)
    tempNode.state = copy(currentNode.state)
    
    x, y = findIndex(tempNode.state, 0)
    if x < 2:
        temp = tempNode.state[x + 1][y]
        tempNode.state[x + 1][y] = 0
        tempNode.state[x][y] = temp
        return tempNode
    else:
        return None


# heuristic function
def manhattanDistance8():

    heuristicEval = 0

    for i in range(0, 8):
        x1, y1 = findIndex(startState, i)
        x2, y2 = findIndex(targetState, i)

        distance = abs(x2 - x1) + abs(y2- y1)
        heuristicEval += distance

    return heuristicEval

# [######### #  #]
# [####      # ##]
# [#### # #    ##]
# [ ##  # # ## ##]
# [#### #########]
  
####### Maze Utilities Start #######
def moveLeftMaze(currentNode):
    global maze

    tempPos = [-1, -1]
    tempPos[0] = currentNode.state[0]
    tempPos[1] = currentNode.state[1]
    x = tempPos[0]
    y = tempPos[1]

    if y > 0 and maze[x][y - 1] != "#":
        tempPos[1] -= 1

    tempNode = Node(tempPos, currentNode, currentNode.cost + 1)
    return tempNode

def moveUpMaze(currentNode):
    global maze

    tempPos = [-1, -1]
    tempPos[0] = currentNode.state[0]
    tempPos[1] = currentNode.state[1]
    x = tempPos[0]
    y = tempPos[1]
    
    if x > 0 and maze[x - 1][y] != "#":
        tempPos[0] -= 1

    tempNode = Node(tempPos, currentNode, currentNode.cost + 1)
    return tempNode

def moveRightMaze(currentNode):
    global maze

    tempPos = [-1, -1]
    tempPos[0] = currentNode.state[0]
    tempPos[1] = currentNode.state[1]
    x = tempPos[0]
    y = tempPos[1]
    
    if y < (mazeWidth - 1) and maze[x][y + 1] != "#":
        tempPos[1] += 1

    tempNode = Node(tempPos, currentNode, currentNode.cost + 1)
    return tempNode

def moveDownMaze(currentNode):
    global maze, mazeHeight, mazeWidth

    tempPos = [-1, -1]
    tempPos[0] = currentNode.state[0]
    tempPos[1] = currentNode.state[1]
    x = tempPos[0]
    y = tempPos[1]

    if x < (mazeHeight - 1) and maze[x + 1][y] != '#':
        tempPos[0] += 1

    tempNode = Node(tempPos, currentNode, currentNode.cost + 1)
    return tempNode


def manhattanDistanceMaze():
    global startPos, targetPos, currentPos
    return abs(targetPos[0] - currentPos[0]) + abs(targetPos[1] - currentPos[1])


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


# current state is a node
def expand8(currentState):
    
    node1 = moveLeft8(currentState)
    node2 = moveUp8(currentState)
    node3 = moveRight8(currentState)
    node4 = moveDown8(currentState)

    children = []
    if node1 != None:
        children.append(node1)
    if node2 != None:
        children.append(node2)
    if node3 != None:
        children.append(node3)
    if node4 != None:
        children.append(node4)
    
    return children


def expandMaze(currentNode):

    node1 = moveLeftMaze(currentNode)
    node2 = moveUpMaze(currentNode)
    node3 = moveRightMaze(currentNode)
    node4 = moveDownMaze(currentNode)

    children = []
    if node1 != None:
        children.append(node1)
    if node2 != None:
        children.append(node2)
    if node3 != None:
        children.append(node3)
    if node4 != None:
        children.append(node4)

    return children

# read file into the variables and structures
def readProblem(fileName):

    global currentPos, maze, mazeHeight, mazeWidth, startPos, targetPos
    global startState, targetState, eightPuzzle
    lines = []

    with open(fileName, 'r') as f:
        line = f.readline()
        if line[0] != '(':
            eightPuzzle = True
            lines.append(line[:-1])
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


        else:
            eightPuzzle = False

            # start position parsing
            index1 = line.index(',')
            index2 = line.index(')')
            sx = line[1:index1]
            sy = line[index1+1:index2]
            startPos.append(int(sx))
            startPos.append(int(sy))
            startPos = startPos[::-1]

            # target position parsing
            line = f.readline()
            index1 = line.index(',')
            index2 = line.index(')')
            tx = line[1:index1]
            ty = line[index1+1:index2]
            targetPos.append(int(tx))
            targetPos.append(int(ty))
            targetPos = targetPos[::-1]

            print("TargetPos:", targetPos)
            row = []
            line = f.readline()
            while line:
                for c in line:
                    if c != '\n':
                        row.append(c)

                maze.append(row)
                line = f.readline()
                row = []
            
            currentPos = startPos
            mazeHeight = len(maze)
            mazeWidth = len(maze[0])

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


def getCost(e):
    return e.cost


def sort():
    global frontier

    if len(frontier) <= 1:
        return frontier
    
    return frontier.sort(reverse=False, key=getCost)


def check(currentNode):

    result = False
    for t in frontier:
        if currentNode == t.state:
            result = True
    
    if currentNode in explored:
        result = True
        
    return result

# Uniform-Cost Search
def UCS():
    global eightPuzzle
    global frontier, explored
    
    if eightPuzzle == True:
        frontier = [Node(startState, None, 0)]
        explored = []

        while len(frontier) > 0:
            sort()
            currentNode = frontier.pop(0)

            if currentNode.state == targetState:
                path = findPath(currentNode)
                return currentNode, path
            explored.extend(currentNode.state)
            children = expand8(currentNode)
            for child in children:
                if check(child.state) == False:
                    frontier.append(child)
                else:
                    for e in frontier:
                        if child.state == e.state and child.cost < e.cost:
                            index = frontier.index(e)
                            frontier[index] = child
                    

        return None

    elif eightPuzzle == False:
        frontier = [Node(startPos, None, 0)]
        explored = []

        while len(frontier) > 0:
            sort()
            currentNode = frontier.pop(0)
            if currentNode.state == [20, 19]:
                print(currentNode.cost)

            if currentNode.state == targetPos:
                result = printPath(currentNode)
                return currentNode, result
            
            explored.extend(currentNode.state)
            children = expandMaze(currentNode)
            for child in children:
                if check(child.state) == False:
                    frontier.append(child)
                else:
                    for e in frontier:
                        if child.state == e.state and child.cost < e.cost:
                            index = frontier.index(e)
                            frontier[index] = child
        return None
        # means maze problem
        

def printPath(currentNode):
    r = []
    while currentNode:
        pos = currentNode.state
        t = (pos[1], pos[0])
        r.append(t)
        currentNode = currentNode.parent

    return r[::-1]


def findDir(arr1, arr2):
    x1, y1 = findIndex(arr1, 0)
    x2, y2 = findIndex(arr2, 0)
    
    if (x2 - x1) == 1:
        return 'UP'
    if (x2 - x1) == -1:
        return 'DOWN'
    if (y2 - y1) == 1:
        return 'LEFT'
    if (y2 - y1) == -1:
        return 'RIGHT'

def findPath(currentNode):
    r = []
    while currentNode and currentNode.parent:
        dir = findDir(currentNode.state, currentNode.parent.state)
        r.append(dir)
        currentNode = currentNode.parent
    
    return r[::-1]


# A* search
def AStar():
    return

def printArr(state):
    for row in state:
        print(row)
    
    return

readProblem("maze1.txt")

result, path = UCS()
print(path)