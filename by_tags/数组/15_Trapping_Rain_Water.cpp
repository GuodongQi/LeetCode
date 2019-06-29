class Solution {
public:
    int trap(vector<int>& height) {
        int size = height.size(), ans = 0;
        if(size == 0) return ans;
        vector<int>left_max(size), right_max(size);
        left_max[0] = height[0];
        right_max[size-1] = height[size-1];
        for(int i=1; i<size;i++)
            left_max[i] = max(left_max[i-1], height[i]);
        for(int i = size-2; i>=0;i--)
            right_max[i] = max(right_max[i+1], height[i]);
        for(int i = 0;i < size; i++)
            ans += min(left_max[i], right_max[i]) - height[i];
        return ans;


    }
};


class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0, current = 0;
        stack<int> stk;
        while(current < height.size()){
            while(!stk.empty() && height[current] > height[stk.top()]){
                int top = stk.top();
                stk.pop();
                if(stk.empty())
                    break;
                int distance = current - stk.top() - 1;
                int bounded_height = min(height[current], height[stk.top()]) - height[top];
                ans += distance * bounded_height;
            }
            stk.push(current++);
        }

        return ans;

    }
};