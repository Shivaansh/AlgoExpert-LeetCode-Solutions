class Solution {
    //Link: https://leetcode.com/problems/min-cost-climbing-stairs/
    // Name: Min Cost Climbing Stairs
    // Difficulty: Easy
    // Topic: Dynamic Programming
    //Time: O(n)
    //Space: O(n)
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        if(cost.size() == 1) {return cost[0];}
        if(cost.size() == 2) {return min(cost[0], cost[1]);}
        
        vector<int> results(cost.size(), 0);
        results[0] = cost[0];
        results[1] = cost[1];
        
        for(int i = 2; i < results.size(); i++)
        {
            results[i] = cost[i] + min(results[i-1], results[i-2]);
        }
        
        int last = results.size()-1;
        return min(results[last], results[last-1]);
    }
};