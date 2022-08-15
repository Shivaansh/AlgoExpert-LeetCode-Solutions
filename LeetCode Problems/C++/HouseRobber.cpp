class Solution {
    /
public:
    int rob(vector<int>& nums) {
        vector<int> results(nums.size(), 0);
        //edge cases
        if(nums.size() == 0) {return 0;}
        if(nums.size() == 1) {return nums[0];}
        if(nums.size() == 2)
        {
            return *max_element(nums.begin(), nums.end());
        }
        
        results[0] = nums[0];
        results[1] = max(nums[0], nums[1]);
        for(int i = 2; i < results.size(); i++)
        {
            results[i] = max((nums[i] + results[i-2]), results[i-1]);
        }
        return results.back();
    }
};