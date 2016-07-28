__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given an integer, write a function to determine if it is a power of two.
'''
def power_of_two(num):
    if num < 0:
        return False
    has_one = False
    while num > 0:
        if num & 1:
            if has_one:
                return False
            else:
                has_one = True
        num >>= 1
    return has_one


if __name__ == '__main__':
    print power_of_two(8)