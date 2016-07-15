__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a sorted array, remove the duplicates in place such that > each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example, Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''

def remove_duplicates_from_sorted_array(array):
    j = 0
    for i in range(1,len(array)):
        if  array[j] != array[i]:
            j += 1
            array[j] = array[i]
    return array[0:j+1]

if __name__ == '__main__':
    array = [1,1,2,3,4,4,4,5,6,6,7,7,8,9]
    print "oring array = ",array
    print "now array = ",remove_duplicates_from_sorted_array(array)