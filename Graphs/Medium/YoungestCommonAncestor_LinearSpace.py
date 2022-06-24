# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    #Name: Youngest Common Ancestor (using linear space)
	#Category and difficulty: Graphs, Medium
    #time: O(d), where d is the depth of the deeper descendant
    #space: O(d), where d is the depth of the deeper descendant
    list1 = []
    list2 = []

    currentOne = descendantOne
    currentTwo = descendantTwo

    while(currentOne is not None):
        list1.append(currentOne)
        currentOne = currentOne.ancestor

    while(currentTwo is not None):
        list2.append(currentTwo)
        currentTwo = currentTwo.ancestor

    list1.reverse()
    list2.reverse()
    
    for i in range(min(len(list1), len(list2))):
        if(list1[i] == list2[i]):
            commonAncestor = list1[i]
    return commonAncestor
    pass
