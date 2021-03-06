class Solution {
    public:
    int uniquePathsWithObstacles(const vector<vector<int> >& obstacleGrid) {
        const int m = obstacleGrid.size();
        const int n = obstacleGrid[0].size();
        if (obstacleGrid[0][0] || obstacleGrid[m - 1][n - 1])
            return 0;
        f = vector<vector<int> >(m, vector<int>(n, 0));
        f[0][0] = obstacleGrid[0][0] ? 0 : 1;
        return dfs(obstacleGrid, m - 1, n - 1);
    }
    private:
    vector<vector<int> > f; //

    // return (0, 0) (x, y)
    int dfs(const vector<vector<int> >& obstacleGrid, int x, int y) {

        if (x < 0 || y < 0) return 0; // // (x,y)

        if (obstacleGrid[x][y]) return 0;
        if (x == 0 and y == 0) return f[0][0]; //

        if (f[x][y] > 0) {
            return f[x][y];
        } else {
            return f[x][y] = dfs(obstacleGrid, x - 1, y) + dfs(obstacleGrid, x, y - 1); }
}
};