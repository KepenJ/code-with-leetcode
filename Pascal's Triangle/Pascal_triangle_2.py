__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3, Return [1,3,3,1].

O(k)
'''

def pascal_triangle_2(row_num):
    if  row_num == 0:
        return
    array = [0 for i in range(row_num)]
    array[0] = 1
    i = 0
    while i < row_num+1:
        j = i-1
        i += 1
        while j >= 1:
            array[j] = array[j]+array[j-1]
            j -= 1
    array[-1] = 1
    return array

if __name__ == '__main__':
    print pascal_triangle_2(7)
