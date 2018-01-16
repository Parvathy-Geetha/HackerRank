"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
 
 Have two pointers, fast and slow.
 fast goes till the position specfied and then slow starts moving from the head.
 
 At any point, the difference between fast and slow is position.
"""

def GetNode(head, position):
    i = 0
    fast = head
    slow = head
    while i < position:
        fast = fast.next
        i = i + 1
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    return slow.data