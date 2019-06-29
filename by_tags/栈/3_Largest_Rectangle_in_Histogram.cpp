class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int cur = 0, ans = 0;
        stack<int> stk;
        heights.push_back(0);
        while(cur<heights.size()){
            if(!stk.empty() && heights[cur] < heights[stk.top()]){
                int top = stk.top();
                stk.pop();
                ans = max(ans,heights[top]*(stk.empty()?cur:cur-stk.top() -1));
            }else
                stk.push(cur++);
        }
        return ans;
    }
};