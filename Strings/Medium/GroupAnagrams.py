def groupAnagrams(words):
    #Name: Group Anagrams
	#Category and difficulty: Strings, Medium
    #time: O(m * n log n): m is the number of words and n is the length of the longest word in the input array. We sort m words alphabetically in O(n log n) time
	#space: O(mn) since we return an array with m words each of max possible length n

    #Create hastable and populate it with indices of each anagram
    hashTable = {}

    #Go through m words - O(m)
    for index in range(len(words)):
        word = words[index]
        #sort word of length n in O(n log n) time
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        #Lookup / add to hash table in constant time
        if(sorted_word in hashTable):
            hashTable[sorted_word].append(index)
        else:
            hashTable[sorted_word] = [index]

    #create array to return
    returnArray = []

    #for each anagram, create a group of words using the indices and the original input array and add to returnArray
    #Max m keys - O(m)
    for key in hashTable:
        group = []
        indices = hashTable[key]
        for i in indices:
            group.append(words[i])
        returnArray.append(group)

    return returnArray
        
        
    pass
