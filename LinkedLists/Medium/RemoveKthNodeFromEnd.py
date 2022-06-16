# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    #Name: Remove Kth node from end
	#Category and difficulty: Linked Lists, Medium
    #time: O(n), where n is the length of the linked list
	#space: O(1)

    #Get length of list
    length = 0
    pointer = head
    while(pointer is not None):
        length += 1
        if(pointer.next is None):
            lastPointer = pointer
        pointer = pointer.next
        
    #EDGE CASE: if removing head node
    if(k == length):
        head.value = head.next.value
        head.next = head.next.next
        return

    #navigate to node BEFORE target node
    nodeToRemove = (length - k + 1)
    pointer = head
    i = 1
    while(i < nodeToRemove-1):
        i+=1
        pointer = pointer.next

    #change NEXT to NEXT.NEXT to remove reference to target node
    pointer.next = pointer.next.next     
    pass
