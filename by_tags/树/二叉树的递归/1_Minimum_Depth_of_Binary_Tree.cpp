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
    int minDepth(TreeNode* root) {
        return minDepth(root, false);
    }

    int minDepth(TreeNode *root, bool hasbrother){
        if(!root) return hasbrother?INT_MAX:0;

        return 1 + min(minDepth(root->left, root->right!=nullptr),
                      minDepth(root->right, root->left!=nullptr));
    }
};