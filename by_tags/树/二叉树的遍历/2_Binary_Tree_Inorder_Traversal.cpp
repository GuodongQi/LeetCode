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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode *cur = root, *prev = nullptr;

        while(cur != nullptr){
            if(cur->left == nullptr){
                result.push_back(cur->val);
                prev = cur;
                cur = cur->right;
            }else{
                // 查找前驱
                TreeNode *node = cur->left;
                while(node->right != nullptr && node->right!=cur)
                    node = node->right;
                if(node->right==nullptr){ //没有线索化
                    node->right = cur;
                    // prev = cur;
                    cur = cur->left;
                }else{ //已经线索化
                    result.push_back(cur->val);
                    node->right = nullptr;
                    prev = cur;
                    cur = cur->right;
                }
            }
        }
        return result;

    }
};