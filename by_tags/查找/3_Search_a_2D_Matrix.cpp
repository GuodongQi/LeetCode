class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()) return false;
        int m = matrix.size(), n = matrix.front().size();
        // cout<<m<<n;
        int size = m * n;
        int left = 0, right = m*n -1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            int tmp = matrix[mid/n][mid%n];
            // cout<<tmp;
            if(target == tmp)
                return true;
            else if (target< tmp){
                right = mid - 1 ;
            }else
                left = mid + 1 ;
        }
        return false;
    }
};