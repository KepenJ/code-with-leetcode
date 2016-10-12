__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example: Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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

def DFS(target,sum,r):
    if  r == None:
        return False
    sum = sum + r.root.data
    if  r.root.left == None and r.root.right == None:
        if  sum == target:
            return True
        else:
            return False
    left_result = DFS(target,sum,r.root.left)
    right_result = DFS(target,sum,r.root.right)
    return left_result or right_result

def has_result(target,r):
    if r == None:
        return False
    sum = 0
    return DFS(target,sum,r)

if  __name__ == '__main__':

#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1

    r_0 = BinaryTree()
    r_0.makeTree(1, None, None)
    r_1 = BinaryTree()
    r_1.makeTree(2,None,None)
    r_2 = BinaryTree()
    r_2.makeTree(7,None,None)
    r_3 = BinaryTree()
    r_3.makeTree(4,None,r_0)
    r_4 = BinaryTree()
    r_4.makeTree(13,None,None)
    r_5 = BinaryTree()
    r_5.makeTree(11,r_2,r_1)
    r_6 = BinaryTree()
    r_6.makeTree(8,r_4,r_3)
    r_7 = BinaryTree()
    r_7.makeTree(4,r_5,None)
    r_8 = BinaryTree()
    r_8.makeTree(5,r_7,r_6)

    print has_result(22,r_8)