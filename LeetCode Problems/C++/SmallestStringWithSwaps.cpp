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
    //https://leetcode.com/problems/smallest-string-with-swaps/
    // Name: Smallest String with swaps
    // Difficulty: Medium
    // Topic: Graphs, Union Find
    //Time: O(n log n) for n find and unionSet operations
    //Space: O(n) for space used by hashmap and returned string
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        

        UnionFind uf(s.size());
        string ansString(s.length(), ' ');
        
        
        //Create connections to get connected components
        for(int pair = 0; pair < pairs.size(); pair++)
        {
            if(!uf.connected(pairs[pair][0], pairs[pair][1]))
            {
                uf.unionSet(pairs[pair][0], pairs[pair][1]);
            }
        }
        
        //create hashmap to store vertices connected to each root
        unordered_map<int, vector<int>> hashmap;
        for(int v = 0; v < s.size(); v++)
        {
            int root = uf.find(v);
            hashmap[root].push_back(v);
        }
        
        //for each root, get connected components, find accompanying characters, and put them in correct place in string
        for(auto component : hashmap)
        {
            vector<int> indices = component.second;
            
            vector<char> characters;
            for(int index : indices)
            {
                characters.push_back(s[index]);
            }
            sort(characters.begin(), characters.end());
            
            for(int index = 0; index < indices.size(); index++)
            {
                ansString[indices[index]] = characters[index];
            }
        }
        
        return ansString;
        
    }
};