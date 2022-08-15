/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
    //https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    // Name: Populating Next Right Pointers in each node
    // Difficulty: Medium
    // Topic: Graphs, BFS
    //Time: O(n) for number of nodes
    //Space: O(1) - this is a restriction placed by the problem
public:
    Node* connect(Node* root) {
        //Using BFS in THEORY, by going through each level of the tree using a pointer 
        if(root == NULL){return root;}
        Node* cLvl = root;
        Node* nLvl = cLvl->left;
        
        while(nLvl != NULL)
        {
            cLvl->left->next = cLvl->right;
            if(cLvl->next != NULL)
            {
                cLvl->right->next = cLvl->next->left;
                cLvl = cLvl->next;
            }
            else
            {
                cLvl = nLvl;
                nLvl = cLvl->left;
            }
        }
        return root;
    }
};