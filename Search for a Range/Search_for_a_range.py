__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,

Given [5, 7, 7, 8, 8, 10] and target value 8,

return [3, 4].
'''

def search_range(array,target):
    attion_array = [-1,-1]
    if len(array) <= 1:
        return attion_array
    start = 0
    end = len(array)-1
    while start <= end:
        min = start + (end - start)/2
        if  array[min] >= target:
            end = min - 1
        else:
            start = min + 1
    if  array[start] == target:
        attion_array[0]=start
    else:
        return attion_array

    end = len(array) -1
    while start <= end:
        min = start + (end - start)/2
        if array[min] <= target:
            start = min + 1
        else:
            end = min - 1
    if  array[end] == target:
        attion_array[1] = end
    return attion_array

if __name__ == '__main__':
    array = [5,7,7,8,8,10]
    print search_range(array,8)