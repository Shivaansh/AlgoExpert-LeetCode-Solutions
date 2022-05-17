def caesarCipherEncryptor(string, key):
    #Name: Caesar Cipher Encryption
	#Category and difficulty: Strings, Easy
    #time: O(n)
	#space: O(n)
	
	
	#edge cases
	if(key == 26):
		return string
	newString = ""
	#edge cases
	if(len(string) == 0):
		return newString
	
	#shift characters using formula created
	#this formula was derived via test case creation
	for i in string:
		newOrd = ((ord(i) - 96 + key) % 26) + 96
		if(newOrd == 96):
			newOrd = 122
		newString += str(chr(newOrd))
	return newString
    pass