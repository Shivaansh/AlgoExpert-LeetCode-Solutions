
class Solution {
    //https://leetcode.com/problems/find-if-path-exists-in-graph/
    // Name: Find if path exists in graph 
    // Difficulty: Medium
    // Topic: Graphs, BFS (can also be solved using DFS)
    //Time: O(n) for number of nodes
    //Space: O(n) for number of nodes
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        
        if(n == 1) {return true;}
        set<int> visited;
        unordered_map<int, vector<int>> adjacencyList;
        queue<int> que;
        
        //Build adjacency list
        for(int edge = 0; edge < edges.size(); edge++)
        {
            adjacencyList[edges[edge][0]].push_back(edges[edge][1]);
            adjacencyList[edges[edge][1]].push_back(edges[edge][0]);
        }
        
        //initialize queue
        que.push(source);
        
        while(!que.empty())
        {
            int current = que.front();
            que.pop();
            if(current == destination) {return true;}
            for(int i = 0; i < adjacencyList[current].size(); i++)
            {
                if(visited.find(adjacencyList[current][i]) == visited.end())
                {
                    que.push(adjacencyList[current][i]);
                }
                
            }
            //Mark current node as visited 
            visited.insert(current);
        }
        return false;
        
        
        
    }
};