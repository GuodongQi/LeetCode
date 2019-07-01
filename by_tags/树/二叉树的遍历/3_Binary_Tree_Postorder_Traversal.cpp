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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<const TreeNode *> s;
        // p 为正在访问的结点，q为刚访问的结点
        const TreeNode *p = root, *q = nullptr;

        do{
            while(p!=nullptr){
                s.push(p);
                p = p->left;
            }
            q = nullptr;
            while(!s.empty()){
                p = s.top();
                s.pop();
                // 右孩子已经被访问或者不存在
                if(p->right== q){
                    result.push_back(p->val);
                    q = p;
                }else{
                    //当前结点不能访问，需要二次进栈
                    s.push(p);
                    p = p->right;
                    break;
                }
            }
        }while(!s.empty());
        return result;
    }
};