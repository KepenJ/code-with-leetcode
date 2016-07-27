__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 - 2

[1,3,5,6], 2 - 1

[1,3,5,6], 7 - 4

[1,3,5,6], 0 - 0

'''

def search_insert (array,target):
    if len(array) <= 0:
        return
    start = 0
    end = len(array)-1
    while start <= end:
        min = start + (end - start)/2
        if  array[min] == target:
            return min
        elif array[min] >= target:
            end = min - 1
        else:
            start = min + 1
    return start

if __name__ == '__main__':
    array = [1,3,5,6]
    print search_insert(array,2)