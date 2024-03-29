class Solution {
public:
    //TOP DOWN
//     int minimumDeleteSum(string s1, string s2) {
        
//         int text1Size = s1.size();
//         int text2Size = s2.size();
//         vector<vector<int>> memo;
//         vector<int> zeroes(s2.size(), -1);
//         for(int i = 0; i < s1.size(); i++)
//         {
//             memo.push_back(zeroes);
//         }
//         return helper(s1, (text1Size-1), s2, (text2Size-1), memo); 
//     }
    
//     int helper(string text1, int index1, string text2, int index2, vector<vector<int>> memo)
//     {
//         if(text1 == text2) {return 0;}
//         if(index1 < 0 || index2 < 0)
//         {
//             int sum = 0;
//             if(index1 < 0)
//             {
//                 for(int i = 0; i <= index2; i++)
//                 {
//                     sum = sum + int(text2[i]);
//                 }
//             }
//             if(index2 < 0)
//             {
//                 for(int i = 0; i <= index1; i++)
//                 {
//                     sum = sum + int(text1[i]);
//                 }
//             }
//             return sum;
//         }
//         if(text1[index1] == text2[index2])
//         {
//             if(memo[index1][index2] == -1)
//             {
//                 memo[index1][index2] =  helper(text1, index1-1, text2, index2-1, memo);
//             }
//             return memo[index1][index2];
//         }
//         else
//         {
//             if(memo[index1][index2] == -1)
//             {
//                 memo[index1][index2] =  min(int(text1[index1]) + helper(text1, index1-1, text2, index2, memo), int(text2[index2]) + helper(text1, index1, text2, index2-1, memo));
//             }
//             return memo[index1][index2];
//         }
//     }
    //BOTTOM UP
    int minimumDeleteSum(string s1, string s2) {
       
        vector<vector<int>> scores;
        vector<int> zeroes(s2.size()+1, 0);
        for(int i = 0; i < s1.size()+1; i++)
        {
            scores.push_back(zeroes);
        }
        
        int lastRow = scores.size()-1;
        int lastCol = scores[0].size()-1;
        
        //prepopulate scores with base scores
        for(int i = lastRow-1; i >=0; i--)
        {
            scores[i][lastCol] = scores[i+1][lastCol] + int(s1[i]);
        }
        for(int i = lastCol-1; i >=0; i--)
        {
            scores[lastRow][i] = scores[lastRow][i+1] + int(s2[i]);
        }
        
        for(int row = s1.size()-1; row >= 0; row--)
        {
            for(int col = s2.size()-1; col >= 0; col--)
            {
                if(s1[row] == s2[col])
                {
                    scores[row][col] =  scores[row+1][col+1];
                }
                else
                {
                    scores[row][col] =  min(int(s1[row]) + scores[row+1][col], int(s2[col]) + scores[row][col+1]);
                }
            }
        }
        return scores[0][0];
    }
};

