class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        const int n = triangle.size();

        int f[n][n];
        fill(f[0],f[0]+n*n,0);
        f[0][0] = triangle[0][0];
        // f[1][0] = f[0][0] + triangle[1][0];
        // f[1][1] = f[0][0] + triangle[1][1];

        for(int i = 1; i < n; i++){
            f[i][0] = f[i-1][0] + triangle[i][0];
            for(int j = 1; j<i+1; j++)
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j];
            f[i][i] = f[i-1][i-1] + triangle[i][i];
        }

        int min_sum = INT_MAX;
        for(int i = 0; i<n; i++){
            min_sum = min(min_sum, f[n-1][i]);
        }
        return min_sum;
    }
};