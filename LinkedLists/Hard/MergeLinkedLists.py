# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    #Name: Merge Linked Lists
    #Category and difficulty: Linked Lists, Hard
    #time: O(n + m) for lenghts of the two linked lists
    #space: O(1) for in-place merge

    #Decide which linked list is the head
    head = None
    if(headOne.value > headTwo.value):
        head = headTwo
    else:
        head = headOne

    current = head
    if(current == headOne):
        q = headTwo
    else:
        q = headOne
    previous = None
    temp = q.next

    while(q is not None):
        #make q the next of previous, for this we need current to be STRICTLY greater than q
        while(current is not None and current.value <= q.value):
            previous = current
            current = current.next
        if(current is None or current.value >= q.value):
            if(previous is not None):
                previous.next = q
            q.next = current
            q = temp
            if(temp is not None):
                temp = temp.next 
            else:
                temp = None
            if(previous is not None):
                previous = previous.next
            else:
                previous = None
    return head
