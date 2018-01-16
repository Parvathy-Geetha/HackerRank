"""
Author  : Parvathy Geetha
Email ID : pgeetha@andrew.cmu.edu
"""
"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    node = Node(data)
    curr_pos = 0
    temp = head

    if head == None and position == 0:
        head = node
        return head
    if position == 0:
        node.next = head
        head = node
        return head        
    while curr_pos < position - 1 and temp  != None:        
        temp = temp.next
        curr_pos = curr_pos + 1    
    node.next = temp.next
    temp.next = node
    return head
