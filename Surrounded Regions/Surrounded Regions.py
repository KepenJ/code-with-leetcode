__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Question:

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region .

For example,in put
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

'''

input_map = (
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"],
)

box = [[0]*4 for row in range(4)]

def dfs(start_x,start_y):
    distination = (
        (0,1),  #right
        (1,0),  #down
        (0,-1), #left
        (-1,0), #up
    )
    x = start_x
    y = start_y
    for i in range(4):
        tx = x + distination[i][0]
        ty = y + distination[i][1]
        if  tx < 1 or ty < 1 or tx > 2  or ty > 2:
            continue
        if  input_map[tx][ty] != 'X' and box[tx][ty] == 0:
            if tx != 0 and ty != 0 and tx != 3 and ty != 3:
                box[tx][ty] = 1
                dfs(tx,ty)

    return

if __name__ == '__main__':
    print("In put:")
    print()
    string = str()
    for row in input_map:
        for point in row:
            string += str(point) + ' '
        print(string)
        string = ''
    print()

    for i in range(4):
        for j in range(4):
            if input_map[i][j] != 'X':
                box[i][j] = 1
                dfs(i,j)



    print("Out put:")
    print()
    string = str()
    for row in box:
        for num in row:
            string += str(num) + ' '
        print(string)
        string = ''

    # string = str()
    # for row in input_map:
    #     for point in row:
    #         string += str(point) + ' '
    #     print(string)
    #     string = ''
    # print()