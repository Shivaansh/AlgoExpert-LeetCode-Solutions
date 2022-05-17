def runLengthEncoding(string):
    #Name: Run Length Encoding
	#Category and difficulty: Strings, Easy
    #time: O(n)
	#space: O(n)

	start = 0
	point = 0
	result = ""
	count = 1
	while(start < len(string)):
		if(point < len(string)-1 and string[point+1] == string[start]):
			count += 1
			point +=1
			if(count == 9):
				result += str(9) + string[start]
				count = 1
				start = point + 1
				point = start
		else:
			result += str(count) + string[start]
			count = 1
			start = point + 1
			point = start
	return result