/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        queue <Node *> aQueue;

        if (root) { aQueue.push(root); }
        int aCount = 0;

        while (!aQueue.empty()) {
            aCount = aQueue.size();
            Node *aPrev = NULL;
            for (int i=0;i<aCount;i++) {
                Node *aNode = aQueue.front();
                aQueue.pop();

                if (aPrev) { aPrev->next = aNode; }
                aPrev = aNode;

                if (aNode->left ) { aQueue.push(aNode->left ); }
                if (aNode->right) { aQueue.push(aNode->right); }
            }
        }
        return root;
    }
};