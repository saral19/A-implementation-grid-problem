import math
import numpy as np
class Node:
    def __init__(self,x,y,other=None,op=""):
        self.f = 0
        self.g = 0
        self.h = 0
        self.Operator = op
        self.child = []
        self.parent = other
        self.x = x
        self.y = y
        # self.identifier = ""

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def calculateG(self,x,y,srow,scol):
        temp = 0
        if(x==srow and y==scol):
            G = 0
        else:
            print("Inside G")
            print("value of x and y ")
            print(x,y)
            print("value of parent x and y are")
            print(self.parent.x,self.parent.y)
            if((self.x - self.parent.x == 1) and (self.y == self.parent.y)):
                temp = 2
            if((self.x == self.parent.x) and (self.y - self.parent.y == 1)):
                temp = 2
            if((self.x-self.parent.x == 1) and (self.y-self.parent.y == 1)):
                temp = 1
            print("value of temp")
            print(temp)
            G = self.parent.g + temp
        # self.g = G
        return G

    def calculateH(self,x,y,grow,gcol):
        a = (x - grow) * (x -grow)
        b = (y -gcol) * (y - gcol)
        temp = math.sqrt(a + b)
        # self.h = temp
        return temp

    def calculateF(self):
        temp = self.g + self.h
        # self.f = temp
        print("F value of ")
        print(self.x,self.y)
        print(temp)
        return temp

    def getOperator(self,x,y):
        if y - self.parent.y == 1 and x == self.parent.x:
            return "R"
        if x - self.parent.x == 1 and y == self.parent.y:
            return "D"
        if y - self.parent.y == 1 and x - self.parent.x == 1:
            return "RD"
        if x - self.parent.x == -1 and y - self.parent.y == 1:
            return "RU"
        if x == self.parent.x and y - self.parent.y == -1:
            return "L"
        if x - self.parent.x == 1 and y - self.parent.y == -1:
            return "LD"
        if x - self.parent.x == -1 and y - self.parent.y == -1:
            return "LU"
        if x - self.parent.x == -1 and y == self.parent.y:
            return "U"
    def setOperator(self,x):
        self.Operator = x

def astar(grid,srow,scol,grow,gcol,glength):
    print("Astar Starts")
    open = []
    closed = []
    startNode = Node(srow,scol)
    startNode.g = startNode.calculateG(srow,scol,srow,scol)
    startNode.h = startNode.calculateH(srow,scol,grow,gcol)
    startNode.f = startNode.calculateF()
    open.append(startNode)
    while len(open) > 0:
        #code to sort on the basis of f value
        open.sort(key=lambda x:x.f)
        current_node = open.pop(0)
        print("current node poopped out")
        print(current_node.x,current_node.y)
        closed.append(current_node)
        print("closed node is")
        for temp in closed:
           print(temp.x,temp.y)
        a = current_node.x
        b = current_node.y
        if grid[a][b] == 'G':
            path = []
            listFinal = []
            path.append('Goal')
            while current_node != startNode:
                path.append(current_node.Operator)
                listFinal.append(tuple(current_node.x,current_node.y,current_node.g))
                current_node = current_node.parent
            path.append('Start')
            path = path[::-1]
            return path
        x1 = current_node.x
        y1 = current_node.y
        neighbour = [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1),(x1-1,y1-1),(x1+1,y1+1),(x1-1,y1+1),(x1+1,y1-1)]
        validNeighbours = []
        for n in neighbour:
            if (n[0] == -1 or n[1] == -1 or n[0] == glength or n[1] == glength):
                continue
            else:
                validNeighbours.append(n)
        print("Valid Neighbours are")
        print(validNeighbours)
        for next in validNeighbours:
            a = next[0]
            b = next[1]
            gridValue = grid[a][b]
            # put other grid check as well
            print(validNeighbours)
            if(gridValue == 'X'):
                tempList = validNeighbours.copy()
                if(x1==a):
                    temp = a + 1
                    if((temp,b) in tempList):
                        validNeighbours.remove((temp,b))
                    temp = a - 1
                    if ((temp, b) in tempList):
                        validNeighbours.remove((temp, b))
                if(y1==b):
                    temp = b + 1
                    if((a,temp) in tempList):
                        validNeighbours.remove((a,temp))
                    temp = b - 1
                    if((a,temp) in tempList):
                        validNeighbours.remove((a, temp))
                continue
            newNode = Node(a,b,current_node)
            newNode.setOperator(newNode.getOperator(a, b))
            if newNode in closed:
                continue
            if newNode in open:
                continue
            print("newNode is created for")
            print(newNode.x,newNode.y)
            newNode.parent = current_node
            current_node.child.append(newNode)
            newNode.g = newNode.calculateG(a,b,srow,scol)
            print("value of G" +str(newNode.g))
            newNode.h = newNode.calculateH(a,b,grow,gcol)
            print("value of H" + str(newNode.h))
            newNode.f = newNode.calculateF()
            print("Value of F" + str(newNode.f))
            open.append(newNode)
            print("Open list is")
            for temp in open:
                print(temp.x,temp.y)
    return None

#map = [['S','R','R','X','G'],['R','X','R','X','R'],['R','R','R','X','R'],['X','R','X','R','R'],['R','R','R','R','X']]
#map = [['S','X','R'],['R','R','X'],['X','R','G']]
#map = [['X','R','G','R'],['S','X','R','R'],['R','R','X','R'],['R','R','R','X']]
map = [['R','S','R','X','G','R'],['R','X','R','X','R','R'],['R','R','X','R','X','R'],['R','R','R','R','X','R'],['R','X','R','X','R','R'],['R','R','R','R','R','R']]
#map = [['S','R','R','R','R','R'],['R','R','R','X','X','R'],['R','X','R','R','R','R'],['R','R','X','R','X','R'],['X','R','R','R','R','R'],['G','R','R','R','X','R']]
listF = np.array(map)
Startrow = 0
Startcol = 0
Goalrow = 0
Goalcol = 0
gridLength = 6
for i in range(len(map)):
    for j in range(len(map[i])):
        if(map[i][j] == 'S'):
            Startrow = i
            Startcol = j
        if(map[i][j] == 'G'):
            Goalrow = i
            Goalcol = j
print(Startrow,Startcol)
print(Goalrow,Goalcol)
path = astar(listF,Startrow,Startcol,Goalrow,Goalcol,gridLength)
# def displayList(listf,srow,scol,flag):
#     tempList = listf.copy()
#     if(flag == 0):
#         tempList[srow][scol] = '*'
#         print(tempList)
#         print()
#         print()
#         print()
#     if(flag == 1 or flag == 2):
#         print(listf)
#         print()
#         print()
#         print()
# def display(path,srow,scol):
#     for i in path:
#         if(i == 'L'):
#             flag = 0
#             scol = scol - 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'R'):
#             flag = 0
#             scol = scol + 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'D'):
#             flag = 0
#             srow = srow + 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'U'):
#             flag = 0
#             srow = srow - 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'RU'):
#             flag = 0
#             scol = scol + 1
#             srow = srow - 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'LU'):
#             flag = 0
#             srow = srow - 1
#             scol = scol - 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'RD'):
#             flag = 0
#             scol = scol + 1
#             srow = srow + 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'LD'):
#             flag = 0
#             scol = scol - 1
#             srow = srow + 1
#             displayList(listF, srow, scol, flag)
#         if(i == 'Start'):
#             flag = 1
#             displayList(listF,srow,scol,flag)
#         if(i == 'Goal'):
#             flag = 2
#             displayList(listF, srow, scol, flag)
# display(path,Startrow,Startcol)
print("Saral")
print()
print(path)
print(listF)
print()
print("Khandelwal")
print("hello")
