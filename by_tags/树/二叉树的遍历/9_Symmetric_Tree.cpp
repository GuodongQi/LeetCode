/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        stack<TreeNode*> s;
        if(!root) return true;
        TreeNode *p = root->left, *q = root->right;
        s.push(p); s.push(q);
        while(!s.empty()) {
            p = s.top(); s.pop();
            q = s.top(); s.pop();
            if (!p && !q) continue;
            if (!p || !q) return false;
            if (p->val != q->val)
                return false;
            s.push(p->left);
            s.push(q->right);

            s.push(q->left);
            s.push(p->right);
        } return true;
    }
};