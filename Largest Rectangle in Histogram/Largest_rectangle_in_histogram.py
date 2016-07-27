__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

http://www.leetcode.com/wp-content/uploads/2012/04/histogram.png

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

http://www.leetcode.com/wp-content/uploads/2012/04/histogram_area.png

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example, Given height = [2,1,5,6,2,3], return 10.
'''

def histogram(array):
    for i in range(len(array)):
        j = i+1
        if  j < len(array)-1:
            sum = 0
            if array[i] < array[j]:
                temp = array[i] * 2
            else:
                temp = array[j] * 2
            if sum <= temp:
                sum = temp
    return sum
if __name__ == '__main__':
    array = [5,2,1,6,2,3]
    print histogram(array)