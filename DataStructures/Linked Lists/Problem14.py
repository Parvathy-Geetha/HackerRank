"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
import sys
def SortedInsert(head, data):
    if head.next == None:
        head.next = Node(data,None, head)
        return head
    temp = head
    while temp.next != None:
        if(data > temp.data):
            temp = temp.next
        else:
            break
    node = Node(data) 
    if temp.next == None and data > temp.data:
        temp.next = node
        node.prev = temp
        return head
    node.next = temp
    node.prev = temp.prev
    temp.prev.next = node
    temp.prev = node
    temp = head
    return head
            