class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        if(numRows == 0) return result;

        result.push_back(vector<int>(1,1)); // 第一行

        for(int i = 2; i<=numRows;++i){
            vector<int> cur(i,1);

            vector<int>&prev = result[i-2];

            for(int j = 1;j<i-1;++j){
                cur[j] = prev[j-1] + prev[j];
            }
            result.push_back(cur);
        }
        return result;

    }
};