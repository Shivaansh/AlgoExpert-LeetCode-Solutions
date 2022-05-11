def tournamentWinner(competitions, results):
	#Name: Tournament Winner
	#Category and difficulty: Arrays, Easy
    #time: O(n)
	#space: O(n)
	currentWinningTeam = ""
	maxWinningTeam = "none"
	scoreTable = {"none" : 0}
    
	for i in range(len(results)):
		#decide winning team
		if(results[i] == 0):
			currentWinningTeam = competitions[i][1]
		else:
			currentWinningTeam = competitions[i][0]
		#update hash table
		if(not (currentWinningTeam in scoreTable)):
			scoreTable[currentWinningTeam] = 0
		scoreTable[currentWinningTeam] += 3
		#update current max
		if(scoreTable[currentWinningTeam] > scoreTable[maxWinningTeam]):
			maxWinningTeam = currentWinningTeam
		
	return maxWinningTeam