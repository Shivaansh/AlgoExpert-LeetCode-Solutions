# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    #Name: Sum of Linked Lists
	#Category and difficulty: Linked Lists, Medium
    #time: O(n), where n is the length of the bigger linked list
	#space: O(n), where n is the lenght of the bigger linked list (this is just order of space used since it can be at most twice as the largest list)
    newLinkedList = None
    sum = getNumFromLList(linkedListOne, 1) + getNumFromLList(linkedListTwo, 1)
    #edge case - single digit sum
    if(sum < 10):
        return LinkedList(sum)
    else:
        #initialize linked list
        head = LinkedList(sum % 10)
        sum = int(sum / 10)
        newLinkedList = head
        #add numbers to linked list
        while(sum > 10):
            head.next = LinkedList(sum % 10)
            head = head.next
            sum = int(sum / 10)
        #add last digit to linked list
        head.next = LinkedList(sum % 10)
        sum = int(sum / 10)
        
    return newLinkedList

def getNumFromLList(linkedList, mult):
    sum = 0
    pointer = linkedList
    while(pointer is not None):
        sum += (pointer.value * mult)
        mult *= 10
        pointer = pointer.next
    return sum
        
