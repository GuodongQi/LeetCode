class Solution {
public:
    int climbStairs(int n) {
        int pre = 0;
        int current = 1;
        for(int i = 1; i<=n; i++){
            int tmp = pre;
            pre = current;
            current += tmp;
        }
        return current;
    }
};