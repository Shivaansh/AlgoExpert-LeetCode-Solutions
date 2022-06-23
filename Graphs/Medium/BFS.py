# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        #Name: Breadth First Search
	    #Category and difficulty: Graphs, Medium
        #time: O(n), where n is the number of nodes
	    #space: O(n), where n is the number of nodes
        queue = [self]
        while(len(queue) > 0):
            currentNode = queue.pop(0)
            for child in currentNode.children:
                queue.append(child)
            array.append(currentNode.name)
        return array
        
        pass
