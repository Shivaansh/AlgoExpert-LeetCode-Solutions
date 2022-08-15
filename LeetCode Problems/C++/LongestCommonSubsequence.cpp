//TOP DOWN APPROACH USED INITIALLY, THEN CONVERTED TO BOTTOM UP
/*
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int text1Size = text1.size();
        int text2Size = text2.size();
        return helper(text1, (text1Size-1), text2, (text2Size-1)); 
    }
    
    int helper(string text1, int index1, string text2, int index2)
    {
        if(index1 < 0 || index2 < 0)
        {
            return 0;
        }
        if(text1[index1] == text2[index2])
        {
            return 1 + helper(text1, index1-1, text2, index2-1);
        }
        else
        {
            return max(helper(text1, index1, text2, index2-1), helper(text1, index1-1, text2, index2));
        }
    }
};
*/
class Solution {
    //https://leetcode.com/problems/longest-common-subsequence/
    // Name: Longest Common Subsequence
    // Difficulty: Medium
    // Topic: 2D Dynamic Programming for 2 strings 
    // Time: O(m * n) for lengths of given strings
    // Space: O(m + n) for lengths of given strings
public:
    int longestCommonSubsequence(string text1, string text2) {
            
        vector<int> previous(max(text1.size(), text2.size())+1, 0);
        for(int row = text1.size()-1; row >= 0; row--)
        {
            vector<int> current(max(text1.size(), text2.size())+1, 0);
            for(int col = text2.size()-1; col >= 0; col--)
            {
                if(text1[row] == text2[col])
                {
                    current[col] = 1 + previous[col+1];
                }
                else
                {
                    current[col] = max(previous[col], current[col+1]);
                }
            }
            previous = current;
        }
        
        return previous[0];
    }
};