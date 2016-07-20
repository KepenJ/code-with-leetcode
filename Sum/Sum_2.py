__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an array of intergers, find two numbers such that they add up to a specific target number. The
function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2 Please note that your returned answers (both index1 and
index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2
'''

def sum_1(array,target):
    index_array = [0 for i in range(2)]
    if  len(array) < 0:
        return index_array
    dic = {}
    for i in range(len(array)):
        dic[array[i]] = i
    for i in range(len(dic)):
        attention = target - array[i]
        if dic.has_key(attention):
            attent_value_index = dic[attention]
            if  attent_value_index != i:
                if attent_value_index > i:
                    index_array[0] = 'index %d'%i
                    index_array[1] = 'index %d'%attent_value_index
                else:
                    index_array[0] = 'index %d'%attent_value_index
                    index_array[1] = 'index %d'%i
            else:
                continue
    return index_array

if __name__ == '__main__':
    array = [1,2,3,4,5]
    target = 7
    print sum_1(array,target)