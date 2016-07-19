__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''
def merge_sorted_array(array_1,j,array_2,k):
    i = j + k -1
    n = j - 1
    m = k - 1
    while i >= 0:
        if  n > 0 and m > 0:
            if  array_1[n] > array_2[m]:
                array_1[i] = array_1[n]
                n -= 1
            else:
                array_1[i] = array_2[m]
                m -= 1
        elif n > 0:
            array_1[i] = array_1[n]
            n -= 1
        elif m > 0:
            array_1[i] = array_2[m]
            m -= 1
        i -= 1
    return array_1

# def remove_duplicates(array):
#     j = 0
#     for i in range(1,len(array)):
#         if  array[j] != array[i]:
#             j += 1
#             array[j] = array[i]
#     return array[0:j+1]


if  __name__ == '__main__':
    array_1 = [1,2,3,4,5,6,0,0,0,0,0]
    array_2 = [4,5,6,7,8]
    array_3 = merge_sorted_array(array_1,6,array_2,5)
    print array_3
    # print remove_duplicates(array_3)