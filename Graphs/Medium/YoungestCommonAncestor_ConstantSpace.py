# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    #Name: Youngest Common Ancestor (using constant space)
	#Category and difficulty: Graphs, Medium
    #time: O(d), where d is the depth of the deeper descendant
    #space: O(1)
    pointerOne = descendantOne
    pointerTwo = descendantTwo

    depth1 = 0
    depth2 = 0
    
    while(pointerOne is not topAncestor):
        pointerOne = pointerOne.ancestor
        depth1 += 1

    while(pointerTwo is not topAncestor):
        pointerTwo = pointerTwo.ancestor
        depth2 += 1

    if(depth1 > depth2):
        while(depth1 > depth2):
            descendantOne = descendantOne.ancestor
            depth1 -= 1

    elif(depth2 > depth1):
        while(depth2 > depth1):
            descendantTwo = descendantTwo.ancestor
            depth2 -= 1

    while(descendantTwo.name is not descendantOne.name):
        descendantTwo = descendantTwo.ancestor
        descendantOne = descendantOne.ancestor

    return descendantOne
    pass
