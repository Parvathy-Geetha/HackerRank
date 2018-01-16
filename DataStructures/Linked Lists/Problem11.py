"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head == None:
        return head
    i = head
    while i != None:
        j = i.next
        prev = i
        while j != None:
            if(j.data == i.data):
                prev.next = j.next
                j = prev
            prev = j
            j = j.next
            
        i = i.next
    return head