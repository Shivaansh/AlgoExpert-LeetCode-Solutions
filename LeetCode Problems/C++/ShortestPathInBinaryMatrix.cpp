class Solution {
    //https://leetcode.com/problems/shortest-path-in-binary-matrix/
    // Name: Shortest Path In Binary Matrix
    // Difficulty: Medium
    // Topic: Graphs, BFS
    //Time: O(n) for number of nodes
    //Space: O(n) for MAX size of queue
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int maxSize = grid.size()-1;
        
        if(grid[maxSize][maxSize] == 1 || grid[0][0] == 1)
        {
            return -1;
        }
        
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}, {-1,-1}, {-1,1}, {1,-1}, {1,1}};
        
        //Queue takes coordinates
        queue<vector<int>> que;
        
        int startingValue = 0;
        //mark start as seen
        grid[0][0] = 1;
        
        vector<int> start = {0, 0, 1};
        vector<int> end = {maxSize, maxSize};
        
        que.push({start});
        while(!que.empty())
        {
            vector<int> current = que.front();
            que.pop();
            //Mark visited
            int row = current[0];
            int col = current[1];
            int distance = current[2];
            if(row == maxSize and col == maxSize) 
            {
                return distance;
            }            
            
            
            
            grid[row][col] = 1;
            //Adding neighbors to queue
            vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}, {-1,-1}, {-1,1}, {1,-1}, {1,1}};
            for(int i = 0; i < directions.size(); i++)
            {
                int nRow = row + directions[i][0];
                int nCol = col + directions[i][1];
                
                if(nCol >= 0 && nCol <= maxSize && nRow >= 0 && nRow <= maxSize&& grid[nRow][nCol] == startingValue)
                {
                    que.push({nRow, nCol, distance+1});
                    grid[nRow][nCol] = 1;
                }
            }
        }
        return -1;
    }
};