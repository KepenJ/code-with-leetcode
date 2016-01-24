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



destination_x = 4
destination_y = 4
start_x = 0
start_y = 0

maze = (
    (0, 1, 0, 0, 0),
    (0, 1, 0, 1, 0),
    (0, 0, 0, 0, 0),
    (0, 1, 1, 1, 0),
    (0, 0, 0, 1, 0),
)
way = [[0]*5 for row in range(5)]

def dfs (x,y,step):
    next = ((1,0),(0,1),(-1,0),(0,-1))
    if  x == destination_x and y == destination_y:
        print(step)
        return
    for i in range(0,4):
        p_x = x + next[i][0]
        p_y = y + next[i][1]
        if  p_x < 0 or p_y < 0 or p_x > 4 or p_y > 4:
            continue
        if  maze[p_x][p_y] == 0 and way[p_x][p_y] == 0:
            way[p_x][p_y] = 1
            dfs(p_x,p_y,step+1)
            way[p_x][p_y] = 0
    return


if __name__ == '__main__':
    way[start_x][start_y] = 1
    dfs(start_x,start_y,0)