#include <vector>
using namespace std;

int numberOfWaysToMakeChange(int n, vector<int> denoms)
{
    /*
    #Name: Number of ways to make change
    #Category and difficulty: Dymamic Programming, Medium
    #time: O(n * d) where n is the given number and d is the number of denominations of coins
    #space: O(n)
    */

    if (n == 0)
    {
        return 1;
    }
    if (denoms.size() == 0)
    {
        return 0;
    }

    int nDenoms = denoms.size();
    vector<int> nWays(n + 1, 0);
    nWays[0] = 1;

    for (int denomIndex = 0; denomIndex < nDenoms; denomIndex++)
    {
        int denominator = denoms[denomIndex];
        for (int i = 1; i <= n; i++)
        {
            if (i - denominator >= 0)
            {
                nWays[i] = nWays[i] + nWays[i - denominator];
            }
        }
    }

    return nWays.back();
}
