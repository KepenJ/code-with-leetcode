__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''

Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?

For example, Given sorted array A = [1,1,2,3,4,4,4,5,6,6,7,7,8,9],

Your function should return length = 13, and A is now [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9].
'''

def remove_duplicates_from_sorted_array(array,duplicates_num = 0):
    j = 0
    num = 0
    for i in range(1,len(array)):
        if  array[j] == array[i]:
            num += 1
            if num < duplicates_num:
                j += 1
                array[j] = array[i]
        else:
            j += 1
            array[j] = array[i]
            num = 0
    return array[0:j+1]

if __name__ == '__main__':
    array = [1,1,2,3,4,4,4,5,6,6,7,7,8,9]
    print "oring array = ",array
    print "now array = ",remove_duplicates_from_sorted_array(array,2)