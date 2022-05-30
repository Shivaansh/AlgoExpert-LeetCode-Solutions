def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    #Name: Tandem Bicycle
    #Category and difficulty: Greedy Algorithms, Easy
    #time: O(n log n) since we sort the input array
    #space: O(1)

    if(len(redShirtSpeeds) == 0):
        return 0
        
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    maxRed = max(redShirtSpeeds)
    maxBlue = max(blueShirtSpeeds)

    if(maxBlue >= maxRed and fastest == True):
        reverseArray(redShirtSpeeds)
    elif(maxRed >= maxBlue and fastest == True):
        reverseArray(blueShirtSpeeds)

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed


def reverseArray(array):
    lo = 0
    hi = len(array) - 1

    while(lo < hi):
        temp = array[lo]
        array[lo] = array[hi]
        array[hi] = temp
        lo += 1
        hi -= 1
        