__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row. For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

'''

def search_matrix(array,target):
    if  len(array) <= 0 or len(array[0]) <= 0:
        return False
    else:
        i = 0
        j = len(array[0])-1
        while i < len(array) and j >= 0:
            if  array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False


if __name__ == "__main__":
    array = [
                [1,   3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ]
    print search_matrix(array,16)


