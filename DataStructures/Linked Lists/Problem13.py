"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""       
def FindMergeNode(headA, headB):
    i = headA
    j = headB
    while( i.next != None ):
        i = i.next
    i.next = headA
    fast = headB
    slow = headB
    #Detect a node in the loop
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    slow = headB
    while( slow != fast):
        slow = slow.next
        fast = fast.next
    return slow.data
            