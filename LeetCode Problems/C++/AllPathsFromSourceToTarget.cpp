class Solution {
    //https://leetcode.com/problems/all-paths-from-source-to-target/
    // Name: All paths from source to target
    // Difficulty: Medium
    // Topic: Graphs, BFS
    //Time: O(2^n * n) for number of paths
    //Space: O(2^n * n) for number of paths
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        if(graph.size() == 0) {return {};}
        if(graph.size() == 1) {return graph;}
        queue<vector<int>> que;
        
        int target = graph.size()-1;
        vector<vector<int>> allPaths;
        
        //given graph is of the form of an adjacency list so use that
        que.push({0});
        
        while(!que.empty())
        {
            vector<int> currentPath = que.front();
            que.pop();
            //lastNode of path is the last element of the path popped from que
            int lastNode = currentPath.back();
            if(lastNode == target)
            {
                allPaths.push_back(currentPath);
                continue;
            }
            //create new path using all elements which have branches to new path
            for(int i = 0; i < graph[lastNode].size(); i++)
            {
                if(graph[lastNode][i] != 0)
                {
                    vector<int> newPath = currentPath;
                    newPath.push_back(graph[lastNode][i]);
                    que.push(newPath);
                }
            } 
        }
        return allPaths;
    }
};