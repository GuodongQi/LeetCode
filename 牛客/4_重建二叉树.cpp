/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        TreeNode *root = reConstr(pre, 0, pre.size()-1, vin, 0, vin.size()-1);
        return root;
    }

    TreeNode * reConstr(vector<int> pre, int p_begin, int p_end, vector<int> vin, int v_begin, int v_end){
        if(p_begin > p_end || v_begin > v_end)
            return nullptr;
        TreeNode *root = new TreeNode(pre[p_begin]);
        for(int i = v_begin; i<=v_end; i++)
            if(vin[i] == pre[p_begin]){
                root->left = reConstr(pre, p_begin + 1, p_begin + i - v_begin, vin, v_begin, i-1);
                root->right = reConstr(pre, p_begin + i - v_begin + 1, p_end, vin, i+1, v_end);
                break;
            }
        return root;
    }


};