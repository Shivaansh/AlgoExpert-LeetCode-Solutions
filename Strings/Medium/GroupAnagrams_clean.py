def groupAnagrams(words):
    #Name: Group Anagrams
	#Category and difficulty: Strings, Medium
    #time: O(m * n log n): m is the number of words and n is the length of the longest word in the input array. We sort m words alphabetically in O(n log n) time
	#space: O(mn) since we return an array with m words each of max possible length n

    #Create hastable and populate it with indices of each anagram
    hashTable = {}
    for index in range(len(words)):
        word = words[index]
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        if(sorted_word in hashTable):
            hashTable[sorted_word].append(words[index])
        else:
            hashTable[sorted_word] = [words[index]]
            
    return list(hashTable.values())
            
    pass
