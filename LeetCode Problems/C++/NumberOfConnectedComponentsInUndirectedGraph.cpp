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
    //https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    // Name: Number of Connected Components in an Undirected Graph
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(e log e) where e is number of edges (Union Find find and union operations are log n time)
    //Space: O(n) for space used by union find to record roots
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        
        UnionFind uf = UnionFind(n);
        
        for(int i = 0; i < edges.size(); i++)
        {
            if(!uf.connected(edges[i][0], edges[i][1]))
            {
                uf.unionSet(edges[i][0], edges[i][1]);
            }
        }
        
        return uf.components();
    }
};