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
    int maxDepth(TreeNode* root) {
        return maxed(root, false);
    }

    int maxed(TreeNode* root, bool hasbrother){
        if(!root) return hasbrother?1:0;

        return 1+max(maxed(root->left, root->right!=nullptr),
                    maxed(root->right, root->left!=nullptr));

    }
};