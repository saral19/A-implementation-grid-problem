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

    def calculateG(self,x,y):
        temp = 0
        if(x==0 and y==0):
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

    def calculateH(self,x,y):
        a = (x - 0) * (x -0)
        b = (y -2) * (y - 2)
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
            return "Right"
        if x - self.parent.x == 1 and y == self.parent.y:
            return "Down"
        if y - self.parent.y == 1 and x - self.parent.x == 1:
            return "Right Down"
        if x - self.parent.x == -1 and y - self.parent.y == 1:
            return "Right Up"
        if x == self.parent.x and y - self.parent.y == -1:
            return "Left"
        if x - self.parent.x == 1 and y - self.parent.y == -1:
            return "Left Down"
        if x - self.parent.x == 1 and y - self.parent.j == 1:
            return "Left Up"
        if x - self.parent.x == -1 and y == self.parent.y:
            return "Up"
    def setOperator(self,x):
        self.Operator = x

def astar(grid):
    print("Astar Starts")
    open = []
    closed = []
    startNode = Node(0,0)
    startNode.g = startNode.calculateG(0,0)
    startNode.h = startNode.calculateH(0,0)
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
            while current_node!=startNode:
                path.append(current_node.Operator)
                current_node = current_node.parent
            return path[::-1]
        x1 = current_node.x
        y1 = current_node.y
        neighbour = [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1),(x1-1,y1-1),(x1+1,y1+1),(x1-1,y1+1),(x1+1,y1-1)]
        validNeighbours = []
        for n in neighbour:
            if (n[0] == -1 or n[1] == -1 or n[0] == 3 or n[1] == 3):
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
            newNode.g = newNode.calculateG(a,b)
            print("value of G" +str(newNode.g))
            newNode.h = newNode.calculateH(a,b)
            print("value of H" + str(newNode.h))
            newNode.f = newNode.calculateF()
            print("Value of F" + str(newNode.f))
            open.append(newNode)
            print("Open list is")
            for temp in open:
                print(temp.x,temp.y)
    return None

#map = [['X','R','G','R'],['S','X','R','R'],['R','R','X','X'],['R','R','R','X']]
map = [['S','X','R'],['R','R','X'],['X','R','G']]
listF = np.array(map)
path = astar(listF)
print("Saral")
print()
print(path)
print()
print("Khandelwal")
print("hello")
