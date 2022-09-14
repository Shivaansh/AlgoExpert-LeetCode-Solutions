# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    #Name: Reverse Linked List
    #Category and difficulty: Linked Lists, Hard
    #time: O(n)
    #space: O(1)
    q = head
    r = None
    while(q != None):
        p = q.next
        q.next = r
        r = q
        q = p
    return r
