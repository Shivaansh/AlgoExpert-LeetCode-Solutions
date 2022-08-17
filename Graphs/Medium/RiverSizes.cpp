#include <vector>
using namespace std;

vector<int> riverSizes(vector<vector<int>> matrix) {
//  #Name: River Sizes
// 	#Category and difficulty: Graphs, Medium
//  #time: O(rc), where r and c are the number of rows and columns in the matrix
// 	#space: O(rc), where r and c are the number of rows and columns in the matrix
  vector<int> sizes;
  int maxRow = matrix.size()-1;
  int maxCol = matrix[0].size()-1;
  for(int row = 0; row < matrix.size(); row++)
    {
      for(int col = 0; col < matrix[0].size(); col++)
        {
          if(matrix[row][col] == 1)
          {
            int size = 0;
            queue<vector<int>> que;
            que.push({row, col});
            
            while(!que.empty())
            {
                vector<int> currentCell = que.front();
                que.pop();

                int cRow = currentCell[0];
                int cCol = currentCell[1];

                if(matrix[cRow][cCol] == 1)
                {
                  size++;
                  matrix[cRow][cCol] = -1;

                  if(cRow-1 >= 0)
                  {
                    // up
                    que.push({cRow-1, cCol});
                  }
                  
                  if(cRow+1 <= maxRow)
                  {
                    // down
                    que.push({cRow+1, cCol});
                  }

                  if(cCol-1 >= 0)
                  {
                    // left
                    que.push({cRow, cCol-1});
                  }

                  if(cCol+1 <= maxCol)
                  {
                    // right
                    que.push({cRow, cCol+1});
                  } 
                }
              
            }
            sizes.push_back(size);
          }
        }
    }

  for(int row = 0; row <= maxRow; row++)
    {
      for(int col = 0; col <= maxCol; col++)
        {
          cout << " | " << matrix[row][col] << " | ";
        }
      cout << endl;
    }
  
  return sizes;
}
