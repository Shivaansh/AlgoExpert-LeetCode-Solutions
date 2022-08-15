class UnionFind {
public:
    UnionFind(int sz) : root(sz), rank(sz) {
        for (int i = 0; i < sz; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY;
            } else {
                root[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }
    
    int components() {
        int val = 0;
        for(int i = 0; i < root.size(); i++)
        {
            if(root[i] == i)
            {
                val++;
            }
        }
        return val;
    }

private:
    vector<int> root;
    vector<int> rank;
};
class Solution {
    //https://leetcode.com/problems/number-of-provinces/
    // Name: Number of Provinces
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(n^3) for size of matrix
    //Space: O(n) for space used by union find to record roots
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        UnionFind uf = UnionFind(isConnected.size());
        
        for(int cityA = 0; cityA < isConnected.size(); cityA++)
        {
            for(int cityB = 0; cityB < isConnected.size(); cityB++)
            {
                //join cities
                if(isConnected[cityA][cityB] == 1)
                {
                    if(!uf.connected(cityA, cityB))
                    {
                        uf.unionSet(cityA, cityB);
                    }
                }
            }
        }
        
        return uf.components();
    }
};