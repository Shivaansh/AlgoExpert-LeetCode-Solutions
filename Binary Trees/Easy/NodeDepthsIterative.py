def nodeDepths(root):
    #Name: Node Depths (solved using iterative approach)
	#Category and difficulty: Binary Trees, Easy
    #time: O(n) since we vist each node
	#space: O(h) for max height of tree
    sumOfDepths = 0
    nodeStack = [{"node" : root, "depth" : 0}]
    
    while(len(nodeStack) > 0):
        currentNode = nodeStack.pop()
        if(currentNode["node"] is None):
            sumOfDepths += 0
        else:
            sumOfDepths += currentNode["depth"]
            nodeStack.append({"node" : currentNode["node"].left, "depth" : currentNode["depth"]+1})
            nodeStack.append({"node" : currentNode["node"].right, "depth" : currentNode["depth"]+1})
            
    return sumOfDepths
    pass