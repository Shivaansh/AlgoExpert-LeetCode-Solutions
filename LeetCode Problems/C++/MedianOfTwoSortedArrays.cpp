class Solution {
    //https://leetcode.com/problems/median-of-two-sorted-arrays/
    // Name: Median of Two Sorted Arrays
    // Difficulty: Hard
    // Topic: Sorted arrays, Two Pointers
    // Time: O(m + n) where m and n are lengths of the given arrays
    // Space: O(m + n) where m and n are lengths of the given arrays
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        //Create a new array which is the SORTED version of the merge of both given arrays, sorted in O(m+n) time
        vector<int> mergedArray;
        int i = 0;
        int j = 0;
        
        while(i < nums1.size() && j < nums2.size())
        {
            if(nums1[i] <= nums2[j])
            {
                mergedArray.push_back(nums1[i]);
                i++;
            }else
            {
                mergedArray.push_back(nums2[j]);
                j++;
            }
        }
        
        while(i < nums1.size())
        {
            mergedArray.push_back(nums1[i]);
            i++;
        }
        while(j < nums2.size())
        {
            mergedArray.push_back(nums2[j]);
            j++;
        }
        
        //Edge case
        if(mergedArray.size() == 0){return 0;}
        
        //Check if merged array is of odd or even length and accordingly return the median
        if(mergedArray.size() % 2 == 0)
        {
            int right = (mergedArray.size() / 2);
            int left = right-1;
            double median = (mergedArray[left] + mergedArray[right]) / 2.0;
            return median;
        }
        else
        {
            double median = mergedArray[mergedArray.size() / 2];    
            return median;
        }
    }
};