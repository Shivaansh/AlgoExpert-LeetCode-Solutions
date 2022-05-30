def classPhotos(redShirtHeights, blueShirtHeights):
    #Name: Class Photos
    #Category and difficulty: Greedy Algorithms, Easy
    #time: O(n log n) since we sort the input arrays
    #space: O(1)
    tallestRed = max(redShirtHeights)
    tallestBlue = max(blueShirtHeights)
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if(tallestRed > tallestBlue):
        return redShirtAreTaller(redShirtHeights, blueShirtHeights)
    elif(tallestBlue > tallestRed):
        return blueShirtAreTaller(redShirtHeights, blueShirtHeights)
    return False
    
    
def redShirtAreTaller(redHeights, blueHeights):
    for i in range(len(redHeights)):
        if redHeights[i] <= blueHeights[i]:
            return False
    return True

def blueShirtAreTaller(redHeights, blueHeights):
    for i in range(len(redHeights)):
        if blueHeights[i] <= redHeights[i]:
            return False
    return True