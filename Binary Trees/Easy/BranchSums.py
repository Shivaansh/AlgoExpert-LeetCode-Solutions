#Name: Branch Sums
#Category and difficulty: Binary Trees, Easy
#time: O(n) since we vist each node
#space: O(n) for each node, there is a recursive function call

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Main Function
    sums = []
    runningSum = 0
    getBranchSums(root, runningSum, sums)
    return sums

def getBranchSums(node, runSum, sums):
    # Helper method to be used recursively
    if(node is None):
        return 
    if(node.left is None and node.right is None):
        sums.append(runSum + node.value)
    
    getBranchSums(node.left, runSum + node.value, sums)
    getBranchSums(node.right, runSum + node.value, sums)
    pass
