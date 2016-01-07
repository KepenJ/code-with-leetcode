__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Question:

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''
def reverseWord(wordArr):
    word1 = wordArr[0]
    wordArr[0] = wordArr[-1]
    wordArr[-1] = word1
    newString = ""
    for i in range(0,len(wordArr)):
        if i == len(wordArr)-1:
            newString = newString + wordArr[i]
        else:
            newString = newString + wordArr[i] + " "
    return newString

def judgeWord(s):
    location = 0
    current = 0
    wordArr = list()
    while current < len(s):
        if  s[current]== ' ':
            wordArr.append(s[location:current])
            location = current+1
        elif current == len(s)-1 and s[current] != ' ':
            wordArr.append(s[location:len(s)])
            location = len(s)
        current += 1
    print(wordArr)
    new = reverseWord(wordArr)
    return new
list


if  __name__ == '__main__':
    old = "the sky is blue"
    new = judgeWord(old)
    print(new)
