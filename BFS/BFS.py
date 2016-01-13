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
import struct
from queue import Queue

class Node:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.hadVisited = False

def isValid (V):
    V.x

def BFS(Vs,Ve,allPoint):
    Q = Queue()
    Q.put(Vs)
    visitied = [[]]*5
    Vn = Vw = Vt = Node()
    visitied[0][0].append(Vs)
    Vs.hadVisited = True
    while Q.empty() != True:
        Vn = Q.get()
        for i in range(0:4):
            Vt = direction[i][0]
            Vw = Node(Vn.x)




