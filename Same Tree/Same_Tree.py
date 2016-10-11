__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same values.
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

def solution(r,t):
    if r == None and t == None:
        return True
    elif r == None or t == None:
        return False
    if r.root.data == t.root.data:
        result_left = solution(r.root.left,t.root.left)
        result_right = solution(r.root.right,t.root.right)
        return result_left and result_right
    else:
        return False

if  __name__ == '__main__':

    r_1 = BinaryTree()
    r_1.makeTree(3, None, None)
    r_2 = BinaryTree()
    r_2.makeTree(3, None, None)
    r_3 = BinaryTree()
    r_3.makeTree(2, None, r_1)
    r_4 = BinaryTree()
    r_4.makeTree(2, None, r_2)
    r_5 = BinaryTree()
    r_5.makeTree(1, r_3, r_4)

    r_11 = BinaryTree()
    r_11.makeTree(3, None, None)
    r_22 = BinaryTree()
    r_22.makeTree(3, None, None)
    r_33 = BinaryTree()
    r_33.makeTree(2, None, r_11)
    r_44 = BinaryTree()
    r_44.makeTree(2, None, r_22)
    r_55 = BinaryTree()
    r_55.makeTree(1, r_33, r_44)

    print solution(r_5,r_55)