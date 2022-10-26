# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    #Name: Node Swap
    #Category and difficulty: Linked Lists, Very Hard
    #time: O(n) where n is the number of nodes in the list
    #space: O(1) for in-place swap

    ##TO-DO: Cleanup code to be more modular and reduce repetition
    temp = head
    nNodes = 0
    while(temp is not None):
        nNodes += 1
        temp = temp.next

    if(nNodes <= 1):
        return head

    if(nNodes >= 2):
        newHead  = head.next

    p = head
    q = None
    r = None
    for i in range(2):
        r = q
        q = p
        p = p.next
        s = None
        
    if(nNodes % 2 == 0): #stop when p is none
        while(p is not None):
            #Swapping Nodes
            if(s is not None):
                s.next = q
            q.next = r
            r.next = p
            #Shifting Pointers
            s = r
            p = p.next
            r = r.next
            q = p
            p = p.next

        if(s is not None):
            s.next = q
        q.next = r
        r.next = p
    
    else: #stop when p.next is none
        while(p.next is not None):
            #Swapping Nodes
            if(s is not None):
                s.next = q
            q.next = r
            r.next = p
            #Shifting Pointers
            s = r
            p = p.next
            r = r.next
            q = p
            p = p.next
            
        if(s is not None):
            s.next = q
        q.next = r
        r.next = p

    return newHead

