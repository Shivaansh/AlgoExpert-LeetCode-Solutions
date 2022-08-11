def levenshteinDistance(str1, str2):
    # Reference: https://www.youtube.com/watch?v=We3YDTzNXEk

    #Name: Levenshtein Distance
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(n * m) where n and m are lengths of the 2 strings
	#space: O(n * m) where n and m are lengths of the 2 strings

    nCols = len(str1) #Rows represent str1
    nRows = len(str2) #Cols represent str2

    dpStore = createStoreMatrix(nRows, nCols)

    for c in range(len(str2)):
        for r in range(len(str1)):
            
            #Formula for Levenshtein Distance
            if(str2[c] == str1[r]):
                dpStore[c+1][r+1] = dpStore[c][r]
            else:
                dpStore[c+1][r+1] = 1 + min(dpStore[c][r+1], dpStore[c+1][r], dpStore[c][r])
                
    #Return last value in matrix           
    return dpStore[-1][-1]


def createStoreMatrix(rows, cols):
    matrix = []
    newArray = []

    for i in range(cols+1):
        newArray.append(i)

    matrix.append(newArray)

    for i in range(1, rows+1):
        newArray = [-1]*(cols+1)
        newArray[0] = i
        matrix.append(newArray)

    return matrix