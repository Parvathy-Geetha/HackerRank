'''
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
'''

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head == None:
        return head
    #Returns the new value of head
    if position == 0:
        head = head.next
        return head
    curr_pos  = 0
    temp = head
    while curr_pos < position - 1:
        temp = temp.next
        curr_pos = curr_pos + 1
    
    temp.next = temp.next.next
    return head