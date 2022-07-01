#Name: Min Height BST
#Category and difficulty: BSTs, Medium
#time: O(n) for number of nodes in SORTED array
#space: O(n) for number of nodes in array
def minHeightBst(array):
    lo = 0
    hi = len(array)-1
    root = createSubtree(array, lo, hi)
    return root

#Since the array is sorted, we can use a binary-search-like approach to use the middle element as the root
#for each subtree and recursively create subtrees
def createSubtree(array, lo, hi):
    if(lo > hi):
        return None
    mid = int((lo+hi)/2)
    newNode = BST(array[mid])
    #Using mid-1 and mid+1 to avoid using mid value again and preventing repetition / infinite loops
    newNode.left = createSubtree(array, lo, mid-1)
    newNode.right = createSubtree(array, mid+1, hi)
    return newNode


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
