#include <vector>
using namespace std;

int minNumberOfCoinsForChange(int n, vector<int> denoms)
{
  /*
  #Name: Min Number of Coins For Change
  #Category and difficulty: Dymamic Programming, Medium
  #time: O(n * d) where n is the given number and d is the number of denominations of coins
  #space: O(n)
  */

  if (n <= 0)
  {
    return 0;
  }

  vector<int> minCoins(n + 1, 999999);
  minCoins[0] = 0;

  for (int denIndex = 0; denIndex < denoms.size(); denIndex++)
  {
    int denom = denoms[denIndex];

    for (int i = 1; i <= n; i++)
    {
      int count;
      if (i - denom >= 0)
      {
        count = 1 + minCoins[i - denom];
      }
      else
      {
        count = 0;
      }

      if (count != 0 && count < minCoins[i])
      {
        minCoins[i] = count;
      }
    }
  }

  int minCount = minCoins.back();
  if (minCount != 999999)
  {
    return minCount;
  }
  return -1;
}
