__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example: Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
'''

import sys
class BinaryTreeNode:
    def __init__(self, data, left, right):
        self.left = left
        self.data = data
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def makeTree(self, data, left, right):
        self.root = BinaryTreeNode(data, left, right)
        # left.root = right.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def preOrder(self, r):
        if r.root is not None:
            print(r.root.data)
            if r.root.left is not None:
                self.preOrder(r.root.left)
            if r.root.right is not None:
                self.preOrder(r.root.right)

    def inOrder(self, r):
        if r.root is not None:
            if r.root.left is not None:
                self.inOrder(r.root.left)
            print(r.root.data)
            if r.root.right is not None:
                self.inOrder(r.root.right)

    def postOrder(self, r):
        if r.root is not None:
            if r.root.left is not None:
                self.preOrder(r.root.left)
            if r.root.right is not None:
                self.preOrder(r.root.right)
            print(r.root.data)

    def levelOrder(self, a):
        q = Queue()
        r = a
        while r is not None:
            print(r.root.data)
            if r.root.left is not None:
                q.add(r.root.left)
            if r.root.right is not None:
                q.add(r.root.right)
            if q.isEmpty():
                print("empty")
                r = None
            else:
                r = q.delete()

def get_heigh(r):
    heigh = 0
    if  r == None:
        return heigh
    leff = get_heigh(r.root.left)
    right = get_heigh(r.root.right)
    if leff > right:
        heigh = leff+1
    else:
        heigh = right+1
    return heigh
'''

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

'''
def solution_1(array,r,level):
    if  r == None:
        return
    array[level].append(r.root.data)
    solution_1(array,r.root.left,level+1)
    solution_1(array,r.root.right,level+1)

'''
return its level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''
def solution_2(array,r,level):
    if  r == None:
        return
    array[level].append(r.root.data)
    solution_2(array,r.root.left,level-1)
    solution_2(array,r.root.right,level-1)

if __name__ == '__main__':
    r_1 = BinaryTree()
    r_1.makeTree(7,None,None)
    r_2 = BinaryTree()
    r_2.makeTree(15,None,None)
    r_3 = BinaryTree()
    r_3.makeTree(20,r_2,r_1)
    r_4 = BinaryTree()
    r_4.makeTree(9,None,None)
    r_5 = BinaryTree()
    r_5.makeTree(3,r_4,r_3)
    heigh = get_heigh(r_5)

    if heigh != 0:
        print "Question 1:"
        array = [([]*2) for i in range(heigh)]
        solution_1(array,r_5,0)
        for i in range(len(array)):
            print array[i]

        print ""
        print "Question 2:"
        array_1 = [([]*2) for i in range(heigh)]
        solution_2(array_1,r_5,heigh-1)
        for i in range(len(array_1)):
            print array_1[i]



