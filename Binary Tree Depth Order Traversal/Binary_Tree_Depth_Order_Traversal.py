__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-



'''
Given a binary tree, return the preorder traversal of its nodes' values.
For example: Given binary tree {1,#,2,3},

      1
     / \
    2   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
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

'''
Binary Tree Preorder Traversal
'''
def solution_preorder(r):
    result_array = []
    if  r == None:
        return result_array
    node_stack = []
    node_stack.append(r)
    while  len(node_stack) != 0:
        node = node_stack.pop()
        result_array.append(node.root.data)
        if node.root.right != None:
            node_stack.append(node.root.right)
        if node.root.left != None:
            node_stack.append(node.root.left)
    return result_array

'''
Binary Tree Inorder Traversal
'''
def solution_inorder(r):
    result_array = []
    if  r == None:
        return result_array
    node_stack = []
    node = r
    while   node or len(node_stack) != 0:
        while  node != None:
            node_stack.append(node)
            node = node.root.left
        if  len(node_stack) != 0:
            node = node_stack.pop()
            result_array.append(node.root.data)
            node = node.root.right
    return result_array

'''
Binary Tree Postorder Traversal
'''
def solution_postorder(r):
    result_array = []
    if  r == None:
        return result_array
    node_stack = []
    node = None
    node_stack.append(r)
    while   len(node_stack) != 0:
        node_1 = node_stack.pop()
        if (node_1.root.left == None and node_1.root.right == None)or(node != None and (node.root.left or node.root.right)):
            result_array.append(node_1.root.data)
            node = node_1
        else:
            if  node_1.root.right != None:
                node_stack.append(node_1.root.right)
            if  node_1.root.left != None:
                node_stack.append(node_1.root.left)

    return result_array

if __name__ == '__main__':

    #   1
    #  / \
    # 2  3

    r_1 = BinaryTree()
    r_1.makeTree(3,None,None)
    r_2 = BinaryTree()
    r_2.makeTree(2,None,None)
    r_3 = BinaryTree()
    r_3.makeTree(1,r_2,r_1)

    print "preorder",solution_preorder(r_3)
    print "inorder",solution_inorder(r_3)
    print "postorder",solution_postorder(r_3)



