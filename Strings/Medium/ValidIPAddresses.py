def validIPAddresses(string):
    # Write your code here.
    validIPs = []
        
    #first dot position
    for firstDot in range(1, min(len(string), 4)):
        firstPart = str(string[:firstDot])
        if(isPartValid(firstPart)):
            for secondDot in range(firstDot+1, firstDot + min(len(string) - firstDot, 4)):
                secondPart = string[firstDot:secondDot]
                if(isPartValid(secondPart)):
                    for thirdDot in range(secondDot+1,  secondDot + min(len(string) - secondDot, 4)):
                        thirdPart = string[secondDot:thirdDot]
                        fourthPart = string[thirdDot:]
                        if(isPartValid(thirdPart) and isPartValid(fourthPart)):
                            validIPs.append((firstPart + "." + secondPart + "." + thirdPart + "." + fourthPart))
    return validIPs
                        
def isPartValid(string):
    if(len(string) >= 2 and string[0] == '0'):
        return False
    if(len(string) > 3 or len(string) == 0 or int(string) < 0 or int(string) > 255):
        return False
    return True
