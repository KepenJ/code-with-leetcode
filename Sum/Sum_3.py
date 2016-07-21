__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: Elements in a triplet (a,b,c) must be in non-descending order.
(ie,a <= b <= c) The solution set must not contain duplicate triplets.
'''

def sum_3(array,target):
    if len(array) < 3:
        return
    for i in range(len(array)-2):
        a = array[i]
        j = i + 1
        k = len(array) - 1
        while j < k:
            b = array[j]
            c = array[k]
            if a + b + c == target:
                print "%d + %d + %d = %d"%(a,b,c,target)
                j += 1
                k -= 1
            elif  a + b + c < target:
                j += 1
            else:
                k -= 1



if __name__ == '__main__':
    array = [0,1,2,3,4,5,6,7,8,9]
    sum_3(array,10)