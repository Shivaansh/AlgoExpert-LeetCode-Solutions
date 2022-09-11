def minRewards(scores):
    #Name: Min Rewards
	#Category and difficulty: Arrays, Hard
    #time: O(n)
	#space: O(n)

    #edge case
    if(len(scores) == 1):
        return 1
    #O(n) space
    rewards = [1] * len(scores) 

    #O(n) time
    #forward pass - pass I
    for index in range(len(scores)-1):
        if(scores[index] < scores[index+1]):
            rewards[index+1] = rewards[index] + 1
            
    #O(n) time
    #reverse pass - pass II
    for index in reversed(range(1, len(scores)-1)):
        if(scores[index-1] > scores[index]):
            #check that you're not REDUCING an already higher score
            if(rewards[index-1] < rewards[index] + 1):
                rewards[index-1] = rewards[index] + 1
                
    #O(1) time - update first and last reward
    if(scores[0] > scores[1]):
        rewards[0] = rewards[1] + 1
    if(scores[len(scores)-1] > scores[len(scores)-2]):
        rewards[len(scores)-1] = rewards[len(scores)-2] + 1
        
    #O(n) time
    sum = 0
    for reward in rewards:
        sum += reward
    return sum