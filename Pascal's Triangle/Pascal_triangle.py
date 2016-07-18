__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5, Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def pascal_traingle(num):
    if  num == 0:
        return
    array = [[0 for i in range(i+1)] for i in range(num)]
    for i in range(num):
        array[i][0] = 1
        array[i][-1] = 1
        j = 1
        while j < len(array[i])-1:
            array[i][j] = array[i-1][j-1] + array[i-1][j]
            j += 1
    return array

if __name__ == '__main__':
    num = 1
    print pascal_traingle(num)