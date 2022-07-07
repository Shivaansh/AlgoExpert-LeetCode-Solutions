def phoneNumberMnemonics(phoneNumber):
    #Name: Phone Number Mnemonics
	#Category and difficulty: Recursion, Medium
    #time: O(4^n * n)
	#space: O(4^n * n) for depth of recursive stack
    keypad = {
        '1' : ['1'], 
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z'],
        '0' : ['0']
    }
    allMnemonics = []
    currMnemonic = ['!'] * len(phoneNumber)
    helper(0, currMnemonic, phoneNumber, allMnemonics, keypad)
    return allMnemonics

def helper(indexInString, currentMnemonic, inputString, allMnemonics, keypad):
    #Base case
    if(indexInString == len(inputString)):
        if(currentMnemonic is not None and len(currentMnemonic) > 0 and currentMnemonic not in allMnemonics):
            allMnemonics.append(''.join(currentMnemonic))
    #Recursive Step
    else: 
        currentNumber = str(inputString[indexInString])
        letters = keypad[currentNumber]
        #This loop runs a max of 4 times, and runs upto 4^n times where n is length of phoneNumber
        for letter in letters:
            currentMnemonic[indexInString] = letter
            helper(indexInString+1, currentMnemonic, inputString, allMnemonics, keypad)