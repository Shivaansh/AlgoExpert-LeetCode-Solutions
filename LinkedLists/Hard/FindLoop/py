# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    #Name: Find Loop
    #Category and difficulty: Linked Lists, Hard
    #time: O(n)
    #space: O(1)
    p = head.next
    q = head.next.next
    while(p != q):
        p = p.next
        q = q.next.next
    #since p is now already in the loop, we should be able to reach the loop start from p AND from the head
    r = head
    while(p != r):
        p = p.next
        r = r.next
    #the start of loop is equidistant from head and p by mathematical proof
    return r