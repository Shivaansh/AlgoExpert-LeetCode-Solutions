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
    //https://leetcode.com/problems/number-of-operations-to-make-network-connected/
    // Name: Number of Operations to Make Network Connected
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(e log e) for number of connections / edges given
    //Space: O(n) for space used by union find to record roots
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        
        UnionFind uf = UnionFind(n);
        int redundantEdges = 0;
        
        for(int i = 0; i < connections.size(); i++)
        {
            if(!uf.connected(connections[i][0], connections[i][1]))
            {
                uf.unionSet(connections[i][0], connections[i][1]);
            }
            else
            {
                redundantEdges++;
            }   
        }
        
        int nComponents = uf.components();
        
        if(nComponents == 1) {return 0;}
        if(redundantEdges >= nComponents-1)
        {
            return nComponents-1;
        }
        return -1;  
    }
};