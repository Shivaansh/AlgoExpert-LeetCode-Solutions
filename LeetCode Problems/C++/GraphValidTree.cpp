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
    //https://leetcode.com/problems/graph-valid-tree/
    // Name: Graph Valid Tree
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(n) where n and e are number of nodes and edges respectively
    //Space: O(n) for space used by union find to record roots
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        UnionFind uf(n);
        
        //Create graph based on edges
        for(int i = 0; i < edges.size(); i++)
        {
            //return false if nodes are already connected by same root before creating component
            if(uf.connected(edges[i][0], edges[i][1]))
            {
                return false;
            }
            else{
                uf.unionSet(edges[i][0], edges[i][1]);
            }
        }
        
        int root = uf.find(0);
        //check that root for all nodes is same
        for(int i = 1; i < n; i++)
        {
            if(uf.find(i) != root)
            {
                return false;
            }
        }
        return true;    
    }
};