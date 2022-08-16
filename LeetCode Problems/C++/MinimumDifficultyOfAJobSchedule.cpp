class Solution {
    //https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
    // Name: Minimum Difficulty of a Job Schedule
    // Difficulty: Hard
    // Topic: 2D Dynamic Programming with iteration in states
    // Time: O(n^2 * d) where n is number of jobs and d is days
    // Space: O(n * d) where n is number of jobs and d is days
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        //edge case
        if(d > jobDifficulty.size()) {return -1;}
    
        //create results store
        vector<vector<int>> results;
        for(int i = 0; i < jobDifficulty.size(); i++)
        {
            vector<int> init(d, 99999);
            results.push_back(init);
        }
        
        //base case - populate first column
        for(int i = 0; i <= jobDifficulty.size()-d; i++)
        {
            results[i][0] = hardestJobInRange(0, i, jobDifficulty);
        }
        
        //for each day
        for(int col = 1; col < d; col++)
        {
            //for jobs possible on cuyrrent day
            for(int row = col; row <= jobDifficulty.size() - (d - (col)); row++)
            {
                //create array of possible values for THIS CELL
                vector<int> values;
                
                for(int i = col-1; i < row; i++)
                {
                    values.push_back(results[i][col-1] + hardestJobInRange(i+1, row, jobDifficulty));
                }
                results[row][col] = *min_element(values.begin(),values.end());
            }
        }
        
        return results[jobDifficulty.size()-1][d-1];
    }
    
    
    int hardestJobInRange(int start, int end, vector<int>& jobs)
    {
        if(start == end)
        {
            return jobs[start];
        }
        int max = -99999;
        for(int i = start; i <= end; i++)
        {
            if(jobs[i] > max)
            {
                max = jobs[i];
            }
        }
        return max;
    }
};