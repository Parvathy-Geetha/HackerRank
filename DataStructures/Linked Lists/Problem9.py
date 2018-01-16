"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    head = Node(-1)
    temp = head
    while headA != None and headB != None:
        if(headA.data < headB.data):
            temp.next = headA
            headA = headA.next   
        else:
            temp.next = headB
            headB = headB.next
        temp = temp.next
    while headA != None:
        temp.next = headA
        headA = headA.next
        temp = temp.next
    while headB != None:
        temp.next = headB
        headB = headB.next
        temp = temp.next
    return head.next
