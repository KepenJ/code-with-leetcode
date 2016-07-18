__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''

def pluse_one(array):
    carry = 1
    i = len(array)-1
    while i >= 0:
        temp = array[i]
        array[i] = (temp + carry)%10
        carry = (temp + array[i])/10
        if  carry == 0:
            break
    if  carry == 1:
        newArray = array
        newArray.insert(0,carry)
        return newArray
    else:
        return array
    pass

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8]
    print pluse_one(array)