__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an array and a value, remove all instances of that > value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

def remove_element(value,array):
    j = 0
    for i in range(len(array)):
        if  array[i] == value:
            continue
        array[j]=array[i]
        j += 1
    return j

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,1,1]
    print "oring length = %s"%(len(array))
    print "now length = %s"%remove_element(1,array)