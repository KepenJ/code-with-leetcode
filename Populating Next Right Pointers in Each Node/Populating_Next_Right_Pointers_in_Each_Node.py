__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-



'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space. You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children). For example, Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

'''

import sys
class BinaryTreeNode:
    def __init__(self, data, left, right):
        self.left = left
        self.data = data
        self.right = right
        self.next_point = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def makeTree(self, data, left, right):
        self.root = BinaryTreeNode(data, left, right)

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

'''
Populating Next Right Pointers in Each Node
'''
def next_right(r):
    if  r == None:
        return
    p = r
    first = None
    while  p != None:
        if  first != None:
            first = p.root.left
        if  p.root.left != None:
            p.root.left.root.next_point = p.root.right
        else:
            break
        if  p.root.next_point != None:
            p.root.right.root.next_point = p.root.next_point.root.left
            p = p.root.next_point
            continue
        else:
            p = first
            first = None

'''
Populating Next Right Pointers in Each Node II
'''
def next_right_two(r):
    p = r
    first = None
    last = None
    while p != None:
        if  first != None:
            if  p.root.left != None:
                first = p.root.left
            elif p.root.right != None:
                first = p.root.right
        if  p.root.left != None:
            if  last != None:
                last.root.next_point = p.root.left
            last = p.root.left

        if  p.root.right != None:
            if  last != None:
                last.root.next_point = p.root.right
            last = p.root.right
        if  p.root.next_point != None:
            p = p.root.next_point
        else:
            p = first
            first = None
            last = None


if __name__ == '__main__':
    #     1
    #    / \
    #   2   3
    #  /\   /\
    # 4  5 6  7

    r_4 = BinaryTree()
    r_4.makeTree(4, None, None)
    r_5 = BinaryTree()
    r_5.makeTree(5, None, None)
    r_6 = BinaryTree()
    r_6.makeTree(6, None, None)
    r_7 = BinaryTree()
    r_7.makeTree(7, None, None)
    r_2 = BinaryTree()
    r_2.makeTree(2, r_4, r_5)
    r_3 = BinaryTree()
    r_3.makeTree(3, r_6, r_7)
    r_1 = BinaryTree()
    r_1.makeTree(1, r_2, r_3)

    next_right(r_1)
    # print r_1

    #     1
    #    / \
    #   2   3
    #  /\    \
    # 4  5    7
    r_44 = BinaryTree()
    r_44.makeTree(4, None, None)
    r_55 = BinaryTree()
    r_55.makeTree(5, None, None)
    r_77 = BinaryTree()
    r_77.makeTree(7, None, None)
    r_22 = BinaryTree()
    r_22.makeTree(2, r_44, r_55)
    r_33 = BinaryTree()
    r_33.makeTree(3, None, r_77)
    r_11 = BinaryTree()
    r_11.makeTree(1, r_22, r_33)

    next_right_two(r_11)
    # print  r_11
