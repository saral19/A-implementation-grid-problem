import math
import numpy as np
class Node:
    def __init__(self,x,y,other=None,f=0,g=0,h=0,op=""):
        self.f = f
        self.g = g
        self.h = h
        self.Operator = op
        self.child = []
        self.parent = other
        self.x = x
        self.y = y
        # self.identifier = ""
    def calculateG(self,x,y):
        temp = 0
        if((y - self.parent.y == 1) and (self.parent.x == 0)):
            temp = 2
        if((self.parent.x - 0 == 1) and (self.parent.y == self.parent.x)):
            temp = 2
        if((self.parent.y - 0 == 1) and (self.parent.x - 0 == 1)):
            temp = 1
        if((self.parent.x - 0 == -1) and (self.parent.y - 0 == 1)):
            temp = 1
        if((self.parent.x == 0) and (self.parent.y - 0 == -1)):
            temp = 2
        if((self.parent.x - 0 == 1) and (self.parent.y - 0 == -1)):
            temp = 1
        if((self.parent.x - 0 == 1) and (self.parent.y - 0 == 1)):
            temp = 1
        if((self.parent.x - 0 == -1) and (self.parent.y == self.parent.x)):
            temp = 2
        G = self.parent.g + temp
        self.g = G

    def calculateH(self,x,y):
        a = (x - 2) * (x - 2)
        b = (y - 2) * (y - 2)
        temp = math.sqrt(a + b)
        self.h = temp

    def calculateF(self):
        temp = self.g + self.h
        self.f = temp

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
    print("Start node is created")
    # startNode.x = 0 #need to change this
    # startNode.y = 0 #need to change this
    # goalNode = Node(2,2)
    # goalNode.f = 0
    # goalNode.g = 0
    # goalNode.h = 0
    # goalNode.x = 2 #need to change this
    # goalNode.y = 2 #need to change this
    print("Goal node is created")
    open.append(startNode)
    while len(open) > 0:
        #code to sort on the basis of f value
        open.sort(key=lambda x:x.f)
        current_node = open.pop(0)
        print("current node poopped out")
        closed.append(current_node)
        a = current_node.x
        b = current_node.y
        if grid[a][b] == 'G':
            path = []
            print("inside currentnode =goal node")
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
        for next in validNeighbours:
            a = next[0]
            b = next[1]
            gridValue = grid[a][b]
            # put other grid check as well
            print(validNeighbours)
            if(gridValue == 'X'):
                temp = b+1
                print(a)
                print(temp)
                if((a,temp) in validNeighbours):
                    validNeighbours.pop((validNeighbours.index(a,temp)))
                print("Valid Neighbours list is")
                print(validNeighbours)
                continue
            newNode = Node(a,b,current_node)
            newNode.setOperator(newNode.getOperator(a, b))
            if newNode in closed:
                continue
            print("newNode is created for")
            print(a)
            print(b)
            current_node.child.append(newNode)
            newNode.calculateG(a,b)
            newNode.calculateH(a,b)
            newNode.calculateF()
            for node in open:
                if(newNode == node and newNode.f > node.f):
                    continue
            open.append(newNode)
    return None

map = [['S','X','R'],['R','R','R'],['X','R','G']]
listF = np.array(map)
path = astar(listF)
print("Saral")
print()
print(path)
print()
print("Khandelwal")
