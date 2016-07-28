__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-


'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example, Given nums = [0, 1, 3] return 2.

Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

def missing_number(array):
    x = 0
    i = 0
    while i <= len(array):
        x ^= i
        i += 1
    for n in array:
        x ^= n
    print x

if __name__ == '__main__':
    array = [0,1,3]
    missing_number(array)