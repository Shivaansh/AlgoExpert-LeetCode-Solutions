# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    #Name: remove duplicates from linked list
	#Category and difficulty: Linked Lists, Easy
    #time: O(n)
	#space: O(1)

	currentNode = linkedList
	tempNode = None
	nextNode = currentNode.next
	while(nextNode is not None):
		if(currentNode.value == nextNode.value):
			tempNode = nextNode
			nextNode = tempNode.next
			currentNode.next = nextNode
			tempNode.next = None
		else:
			currentNode = nextNode
			nextNode = currentNode.next
			
    return linkedList
