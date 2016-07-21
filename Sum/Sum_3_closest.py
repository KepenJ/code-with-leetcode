__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
 You man assume that each input would have exactly one solution.
'''

def sum_3_closest(array,target):
    ret = 0
    if len(array) < 3:
        print "length of array is 0"
    distance = 9223372036854775807
    for i in range(len(array)-2):
        j = i+1
        k = len(array)-1
        while j < k:
            temp_sum = array[i] + array[j] + array[k]
            if  temp_sum < target:
                temp_distance = target - temp_sum
                if  temp_distance < distance:
                    distance = temp_distance
                    ret = array[i] + array[j] + array[k]
                j += 1
            elif temp_sum > target:
                temp_distance = temp_sum - target
                if temp_distance < distance:
                    distance = temp_distance
                    ret = array[i] + array[j] + array[k]
                k -= 1
            else:
                ret = array[i] + array[j] + array[k]
                print "%d + %d + %d = %d"%(array[i],array[j],array[k],target)
                return ret

    print "%d nearest %d" % (ret, target)
    return ret

if __name__ == '__main__':
    array = [0,1,2,3,4,5,6,7,8,9,10,11]
    sum_3_closest(array,40)
