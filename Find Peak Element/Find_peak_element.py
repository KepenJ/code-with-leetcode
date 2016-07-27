__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] << -1.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

def find_peak_element(array):
    if  len(array) < 3:
        return 0
    start = 0
    end = len(array) - 1
    while start <= end:
        min = start + (end - start)/2
        if  (min == 0 or array[min] > array[min -1]) and (min == len(array)-1 or array[min] > array[min + 1]):
            return min
        elif min > 0 and array[min] < array[min - 1]:
            end = min - 1
        else:
            start = min + 1
    return min

if __name__ == '__main__':
    array = [1, 2, 3, 1]
    print find_peak_element(array)