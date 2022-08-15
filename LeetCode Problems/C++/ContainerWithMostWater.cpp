class Solution {
    //Link: https://leetcode.com/problems/container-with-most-water/
    // Name: Container with Most Water
    // Difficulty: Medium
    // Topic: Arrays, Two Pointer Technique
    //Time: O(n)
    //Space: O(1)
public:
    int maxArea(vector<int>& height) {
        int lo = 0;
        int hi = height.size()-1;
        int area = 0;
        int maxArea = 0;
        while(lo < hi)
        {
            area = min(height[lo], height[hi]) * abs(lo-hi);
            if(area > maxArea) {maxArea = area;}
            if(height[lo] <= height[hi])
            {
                lo++;
            }
            else
            {
                hi--;
            }
        }  
        return maxArea;
    }
};