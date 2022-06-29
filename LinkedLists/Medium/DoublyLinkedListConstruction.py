# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

#Name: Doubly Linked List Construction
#Category and difficulty: Linked Lists, Medium
#time: Varies for all functions
#space: O(1) for all function

    def setHead(self, node):
        #time: O(1)
        if(self.head is None):
            self.head = node
            self.tail = node
            return
        self.remove(node)
        currentHead = self.head
        currentHead.prev = node
        node.next = currentHead
        node.prev = None
        self.head = node

    def setTail(self, node):
        #time: O(1)
        if(self.head is None):
            self.head = node
            self.tail = node
            return
        self.remove(node)
        currentTail = self.tail
        currentTail.next = node
        node.prev = currentTail
        node.next = None
        self.tail = node

    def insertBefore(self, node, nodeToInsert):
        #time: O(1)
        if(nodeToInsert == self.head and nodeToInsert == self.tail):
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if(node.prev is None):
            self.setHead(nodeToInsert)
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        

    def insertAfter(self, node, nodeToInsert):
        #time: O(1)
        if(nodeToInsert == self.head and nodeToInsert == self.tail):
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if(node.next is None):
            self.setTail(nodeToInsert)
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        #time: O(n), where n is position
        if(position == 1 or self.head is None):
            self.setHead(nodeToInsert)
            return
        currPosition = 1
        pointer = self.head
        while(pointer is not None and currPosition < position):
            currPosition += 1
            pointer = pointer.next
        if(pointer is not None):   
            self.insertBefore(pointer, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        #time: O(n), where n is number of nodes with value
        while(self.containsNodeWithValue(value)):
            pointer = self.head
            while(pointer is not None):
                removedNode = pointer
                pointer = pointer.next
                if(removedNode.value == value):
                    self.remove(removedNode)

    def remove(self, node):
        #time: O(1)
        if(node == self.head):
            self.head = self.head.next
            
        if(node == self.tail):
            self.tail = self.tail.prev

        if(node.prev is not None):
            node.prev.next = node.next
            
        if(node.next is not None):  
            node.next.prev = node.prev
            
        node.prev = None
        node.next = None


    def containsNodeWithValue(self, value):
        #time: O(n) where n is number of nodes
        pointer = self.head
        while(pointer is not None and pointer.value is not value):
            pointer = pointer.next
        return (pointer is not None)
