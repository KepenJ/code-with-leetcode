__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011,so the function should return 3.
'''
import ctypes
def num_of_one(n):
    cout = 0
    while n >0:
        cout += n & 1
        n >>= 1
    return cout

if __name__ == "__main__":

    print num_of_one((ctypes.c_uint32(11).value))