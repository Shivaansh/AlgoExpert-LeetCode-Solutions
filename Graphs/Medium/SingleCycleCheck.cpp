using namespace std;

bool hasSingleCycle(vector<int> array) {
// #Name: Single Cycle Check
// #Category and difficulty: Graphs, Medium
// #time: O(n), where n is the length of the array
// #space: O(1)
  int count = 0;
  int visited = -999999;
  int start = 999999;
  int index = 0;
  
  while(count < array.size())
    {
      //Edge case
      if(array[index] == 0) {return false;}

      //check if reached start or previously visited node before checking all nodes 
      if((array[index] == start || array[index] == visited) && count <= array.size())
      {
        return false;
      }

      //get jump value
      int jump = array[index];

      //Mark current node as either start or visited
      if(index == 0)
      {
        array[index] = start;
      }
      else
      {
        array[index] = visited;
      }
      count++;

      
      index = (index + jump) % (int)array.size();
      if(index < 0)
      {
        index = index + array.size();
      }
      
      if(count > array.size() || array[index] == visited)
      {
        return false;
      }
    }
  
  return true;
}
