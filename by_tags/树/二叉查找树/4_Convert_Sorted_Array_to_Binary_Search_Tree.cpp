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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sorted(nums.begin(), nums.end());
    }
    template<class RandomAccessIterator>
    TreeNode* sorted(RandomAccessIterator first, RandomAccessIterator last){
        const auto length = distance(first, last);
        if(length <= 0) return nullptr;

        auto mid = first + length /2;
        TreeNode* root = new TreeNode(*mid);
        root->left = sorted(first , mid);
        root->right = sorted(mid+1, last);

        return root;
    }
};