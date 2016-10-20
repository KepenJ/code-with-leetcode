__author__ = 'KepenJ'
# -*- coding: UTF-8 -*-


import sys

class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print 'target is not exist!'

    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print 'Linklist is empty.'
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


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
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''
def list_to_BTS(list):
    pass
def build(start,end):
    pass

'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
def array_to_BTS(r):
    pass


if __name__ == '__main__':
    pass
