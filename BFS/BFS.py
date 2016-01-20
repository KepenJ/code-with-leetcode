__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Question : Maze

It represents a labyrinth ,
in which 1 represents the wall ,
0 can be the way to go ,
only to go sideways or vertically to go ,
can not go sideways ,
requiring programmed from the upper left to the lower right corner to find the shortest route.

In put:

int maze[5][5] = {
    0, 1, 0, 0, 0,
    0, 1, 0, 1, 0,
    0, 0, 0, 0, 0,
    0, 1, 1, 1, 0,
    0, 0, 0, 1, 0,
};

Out put:

(0, 0),(1, 0),(2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(3, 4),(4, 4)

'''
from queue import Queue

class Node:
    def __init__(self,x=0,y=0,value=0):
        self.x = x
        self.y = y
        self.hadVisited = False
        if  value == 0:
            self.isWall = False
        else:
            self.isWall = True
        self.count = 0
    def printSelf(self):
        if  self.isWall == True:
            return "X"
        else:
            if  self.hadVisited == True:
                return self.count
            else:
                return 0

    @classmethod
    def NodeAdd(cls,Va,Vb):
        return Node(Va.x+Vb.x,Va.y+Vb.y,max(Va.isWall,Vb.isWall))

def isValid (V):
    if (V.x >= 0 and V.x <= 4) and (V.y >= 0 and V.y <= 4):
        return True
    else:
        return False

def isEndNote(Va,Vb):
    if  Va.x == Vb.x and Va.y == Vb.y:
        return True
    else:
        return False

def BFS(Vs,Ve,outMaze):
    Q = Queue()
    Q.put(Vs)
    visitied = outMaze
    Vs.hadVisited = True
    visitied[0][0] = Vs
    distination = (Node(1,0,0),Node(0,1,0),Node(-1,0,0),Node(0,-1,0))
    count = 1
    while Q.empty() != True:
        Vn = Q.get()
        for i in range(0,4):
            Vw = Node.NodeAdd(Vn,distination[i])
            if  isEndNote(Vw,Ve):
                Vw.hadVisited = True
                Vw.count = count
                visitied[Vw.x][Vw.y] = Vw
                print("The way is:")
                print("(%d,%d)"%(Ve.x,Ve.y))
                showWayNums(Vw,Vs,visitied)
                # printString = str()
                # for i in range(0,len(outMaze)):
                #     Varray = outMaze[i]
                #     for j in range(0,len(Varray)):
                #         V = Varray[j]
                #         printString += str(V.printSelf()) + '   '
                #     printString += '\n'
                # print("Step:\n")
                # print(printString)
                return True
            if  isValid(Vw):
                Vw.isWall = visitied[Vw.x][Vw.y].isWall
                if Vw.isWall != True:
                    if  visitied[Vw.x][Vw.y].hadVisited != True:
                        Q.put(Vw)
                        Vw.hadVisited = True
                        Vw.count = count
                        visitied[Vw.x][Vw.y] = Vw
                        count += 1

    else:
        print("WTF! No result!")
        return False

def showWayNums(Vs,Ve,visitied):
    Q = Queue()
    Q.put(Vs)
    distination = (Node(1,0,0),Node(0,1,0),Node(-1,0,0),Node(0,-1,0))
    while Q.empty() != True:
        Vn = Q.get()
        for i in range(0,4):
            Vw = Node.NodeAdd(Vn,distination[i])
            if  isEndNote(Vw,Ve):
                print("(%d,%d)"%(Ve.x,Ve.y))
                return True
            if  isValid(Vw):
                Vp = visitied[Vw.x][Vw.y]
                if Vp.isWall != True:
                    if  Vp.hadVisited == True and Vp.count < Vn.count:
                        Q.put(Vp)
                        print("(%d,%d)"%(Vp.x,Vp.y))
    else:
        print("WTF!")
        return False


def changeIntToNode():
    maze = (
        0, 1, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 0,
        0, 0, 0, 1, 0,
    )
    outMaze = [[Node()]*5 for row in range(5)]
    k = 0
    for i in range(0,5):
        for j in range(0,5):
            outMaze[i][j] = Node(i,j,maze[k])
            k += 1
    printString = str()
    for i in range(0,len(outMaze)):
        Varray = outMaze[i]
        for j in range(0,len(Varray)):
            V = Varray[j]
            printString += str(V.printSelf()) + ' '
        printString += '\n'
    print("My maze:\n")
    print(printString)
    return outMaze

if  __name__ == '__main__':
    BFS(Node(0,0),Node(4,4,),changeIntToNode())
