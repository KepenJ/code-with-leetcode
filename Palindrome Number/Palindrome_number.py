__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

def is_palindrome_number(num):
    if  num < 0:
        return False
    elif num == 0:
        return True
    else:
        y = 0
        x = num
        while x != 0:
            y = y*10+x%10
            x = x/10
        if y == num:
            return True
        else:
            return False

if __name__ == '__main__':
    print is_palindrome_number(12244221)