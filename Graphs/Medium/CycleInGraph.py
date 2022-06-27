def cycleInGraph(edges):
    #Name: Cycle in Graph
	#Category and difficulty: Graphs, Medium
    #time: O(v+e), where v is number of vertices and e is number of edges
    #space: O(v), where v is number of vertices

    #Edge case
    if(len(edges) == 1):
        return True
    #iterating through vertices
    for vertex in range(len(edges)):
        start = vertex
        stack = []
        #Keeping track of number of vertices visited since the path shouldn't be longer than the number of vertices in case of no cycle
        count = 0
        #Populating stack with the neighbords for the current vertex
        for i in edges[start]:
            stack.append(i)
        #Running DFS
        while(len(stack) > 0 and count <= len(edges)):
            count += 1
            current = stack.pop()
            if(current == start):
                return True
            for nextVertex in edges[current]:
                stack.append(nextVertex)
                
    return False
