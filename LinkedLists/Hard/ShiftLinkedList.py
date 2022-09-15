# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    #Name: Shift Linked Lists
    #Category and difficulty: Linked Lists, Hard
    #time: O(n) for length of the linked list
    #space: O(1)

    #find length of list and find last node - O(n)
    start = head
    last = None
    lengthOfList = 0
    while(start != None):
        lengthOfList += 1
        last = start
        start = start.next
    if(lengthOfList == 1):
        return head

    #set value of k to be used, for both positive and negative cases - O(1)
    k = k % lengthOfList
    if(k == 0):
        return head
    
    #find new head and make necessary connections - O(1)
    newLastIndex = (lengthOfList - k)
    newHeadIndex = newLastIndex + 1
    newLast = None
    newHead = None
    current = head
    ind = 1
    # O(n) at most
    while(ind <= newHeadIndex):
        if(ind == newLastIndex):
            newLast = current
        if(ind == newHeadIndex):
            newHead = current
        current = current.next
        ind += 1
    #O(1)
    last.next = head
    head = newHead
    newLast.next = None
    return newHead