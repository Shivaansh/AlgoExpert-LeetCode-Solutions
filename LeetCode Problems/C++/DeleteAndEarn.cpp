class Solution {
    //Link: https://leetcode.com/problems/delete-and-earn/
    // Name: Delete And Earn
    // Difficulty: Medium
    // Topic: Dynamic Programming
    //Time: O(n)
    //Space: O(n)
public:
    int deleteAndEarn(vector<int>& nums) {
        
        int maxNum = 0; 
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i] > maxNum)
            {
                maxNum = nums[i];
            }
        }
        //scores is the number of points we can get from that specific number
        vector<int> scores(maxNum+1,0); 
        for(int i = 0; i < nums.size(); i++)
        {
            scores[nums[i]] += nums[i];
        }
        //results is to score the result of the bottom up DP approach
        vector<int> results(maxNum+1,0);
        results[0] = 0; // 0 * anything is 0
        results[1] = scores[1]; //depends on whether 1 exists or not in nums
        
        //calculate score for each num starting at 2
        for(int i = 2; i < maxNum+1; i++)
        {
            results[i] = max(scores[i]+results[i-2], results[i-1]);
        }
        
        return results[maxNum];
    }
    
};