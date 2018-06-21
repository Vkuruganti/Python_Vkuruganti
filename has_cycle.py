# Vas Kuruganti
#the function has_cycle in the editor below. It must return a boolean True if the graph contains a cycle, or False.
#has_cycle has the following parameter(s):
#a pointer to a Node object that points to the head of a linked list.
#Note: If the list is empty, head will be null.


"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None: return False
    tortoise = hare = head 
    while hare != None and hare.next != None: 
        tortoise = tortoise.next
        hare = hare.next.next 
        if tortoise == hare: return True # cycle detected 
    return False 
    
