class Solution {
    //Link: https://leetcode.com/problems/n-th-tribonacci-number/
    // Name: N-th Tribonacci Number
    // Difficulty: Easy
    // Topic: Dynamic Programming
    //Time: O(n)
    //Space: O(1)
public:
    int tribonacci(int n) {
        if(n == 0) {return 0;}
        if(n == 1 || n == 2) {return 1;}
        
        int tn1 = 0;
        int tn2 = 1;
        int tn3 = 1;
        
        for(int i = 3; i <= n; i++)
        {
            int tn = tn1 + tn2 + tn3;
            tn1 = tn2;
            tn2 = tn3;
            tn3 = tn;
        }
        return tn3;
    }
};