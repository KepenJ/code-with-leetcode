__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-


'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''
import sys
# Binary tree
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

global num
def min_depth(root):
    global num
    if root == None:
        return
    num = sys.maxsize
    d = 1
    depth(root,d)
    return num

def max_travel(root):
    if root == None:
        return
    num = -sys.maxsize-1
    travel(root,1)
    return num

def travel(node,level):
    global num
    if  node.left != None and node.right != None:
        num = max(num,level)
        return
    if  node.left:
        travel(node.left,level+1)
    if  node.right:
        travel(node.right,level+1)

def depth(node,n):
    global num
    if (node.left == None and node.right == None):
        num = min(num,n)
        return

    if (node.left):
        n += 1
        depth(node.left,n)
        n -= 1

    if (node.right):
        n += 1
        depth(node.right,n)
        n -= 1
if __name__ == '__main__':
    r = BinaryTree()
    ra = BinaryTree()
    ra.makeTree(2, None, None)
    rb = BinaryTree()
    rb.makeTree(3, None, None)
    r.makeTree(1, ra, rb)
    # min_depth(r.root)
    max_travel(r.root)
