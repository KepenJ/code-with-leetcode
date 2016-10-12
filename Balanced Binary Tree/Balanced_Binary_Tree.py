__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    if  r == None:
        return 0
    left_heigh = get_heigh(r.root.left)
    if  left_heigh == -1:
        return -1;
    right_heigh = get_heigh(r.root.right)
    if  right_heigh == -1:
        return -1
    diff_heigh = 0
    if  right_heigh>left_heigh:
        diff_heigh = right_heigh - left_heigh
    else:
        diff_heigh = left_heigh - right_heigh
    if  diff_heigh > 1:
        return -1
    else:
        if right_heigh > left_heigh:
            diff_heigh = right_heigh+1
        else:
            diff_heigh = left_heigh+1
        return diff_heigh

def solution(r):
    if  r == None:
        return True
    is_balance = get_heigh(r)
    if  is_balance != -1:
        return True
    else:
        return False


if  __name__ == '__main__':

#    3
#   / \
#  9  20
#     / \
#    15  7
#         \
#          1

    r_0 = BinaryTree()
    r_0.makeTree(1, None, None)
    r_1 = BinaryTree()
    r_1.makeTree(7,None,r_0)
    r_2 = BinaryTree()
    r_2.makeTree(15,None,None)
    r_3 = BinaryTree()
    r_3.makeTree(20,r_2,r_1)
    r_4 = BinaryTree()
    r_4.makeTree(9,None,None)
    r_5 = BinaryTree()
    r_5.makeTree(3,r_4,r_3)

    print solution(r_5)