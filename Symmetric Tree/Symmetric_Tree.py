__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center)

For example, this tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following tree is not.
    1
   / \
  2   2
   \   \
   3    3
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


def compared(left,right):
    if  left == None and right == None:
        return True
    elif left == None or right == None:
        return False
    result_1 = left.root.data == right.root.data
    result_2 = compared(left.root.left,right.root.right)
    result_3 = compared(left.root.right,right.root.left)
    return result_1 and result_2 and result_3

def solution(r):
    if  r == None:
        return True
    return compared(r.root.left,r.root.right)

if  __name__ == '__main__':


#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3

    r_1 = BinaryTree()
    r_1.makeTree(3,None,None)
    r_2 = BinaryTree()
    r_2.makeTree(4,None,None)
    r_3 = BinaryTree()
    r_3.makeTree(2,r_2,r_1)
    r_4 = BinaryTree()
    r_4.makeTree(3,None,None)
    r_5 = BinaryTree()
    r_5.makeTree(4,None,None)
    r_6 = BinaryTree()
    r_6.makeTree(2,r_4,r_5)
    r_7 = BinaryTree()
    r_7.makeTree(1,r_6,r_3)

#    1
#   / \
#  2   2
#   \   \
#   3    3

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

# reslut
    print solution(r_7)

    print solution(r_55)
