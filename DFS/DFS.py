__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Question : DFS
use 1~9 to put in box,get the true value.
[][][] + [][][] = [][][]

In put:

1~9

Out put:

true value.

124 + 659 = 783
125 + 739 = 864
127 + 359 = 486
127 + 368 = 495
.
.
.

'''
global a
a = [0]* 10
global book
book = [0] * 10

def dfs (step):
    if  step == 10:
        if  a[1]*100+a[2]*10+a[3]*1 +a[4]*100+a[5]*10+a[6] == a[7]*100+a[8]*10+a[9]:
            print("%d%d%d + %d%d%d = %d%d%d"%(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
            return
    for i in range(1,10):
        if  book[i] == 0:
            a[step] = i
            book[i] = 1
            dfs(step+1)
            book[i]= 0
    return

if __name__ == '__main__':
    dfs(1)