class UnionFind {
public:
    UnionFind(int sz) : root(sz), rank(sz) {
        for (int i = 0; i < sz; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    //Optimized using Path Compression
    int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }
    
    //Optimized using Union by Rank
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
    //https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
    // Name: The Earliest Moment When Everyone Become Friends
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(n + m log m) where n and m are number of people and logs respectively
    //Space: O(n + log m) where n and m are number of people and logs respectively
public:
    
    struct less_than_key
    {
        inline bool operator() (vector<int>& log1, vector<int>& log2)
        {
            return (log1[0] < log2[0]);
        }
    };

    
    int earliestAcq(vector<vector<int>>& logs, int n) {
        
        UnionFind uf(n);
        
        sort(logs.begin(), logs.end(), less_than_key());
        
        for(int logIndex = 0; logIndex < logs.size(); logIndex++)
        {
            if(!uf.connected(logs[logIndex][1], logs[logIndex][2]))
            {
                uf.unionSet(logs[logIndex][1], logs[logIndex][2]);
            }
            uf.find(logs[logIndex][1]);
            if(uf.components() == 1) {return logs[logIndex][0];}
        }
        return -1; 
    }
};