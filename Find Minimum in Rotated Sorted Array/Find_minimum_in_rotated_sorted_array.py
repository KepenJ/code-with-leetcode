__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


def fin_min(array):
    if len(array) == 0:
        return
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        if  array[0] >array[1]:
            return array[1]
        else:
            return array[0]
    start = 0
    stop = len(array)-1
    while start < stop -1:
        if array[start] < array[stop]:
            return array[start]
        min = start + (stop - start)/2
        if  array[min] > array[start]:
            start = min
        else:
            stop = min
    if array[start] < array[stop]:
        return array[start]
    else:
        return array[stop]

if __name__ == '__main__':
    array = [4,5,6,7,8,0,1,2,3]
    print "min num is %d"%fin_min(array)