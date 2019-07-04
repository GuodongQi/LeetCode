class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        subsets(nums,path,0,res);
        return res;
    }

    void subsets(vector<int> &S, vector<int> &path, int step, vector<vector<int>> &result){
        if(step == S.size()){
            result.push_back(path);
            return;
        }

        subsets(S, path, step+1,result);
        path.push_back(S[step]);
        subsets(S, path, step+1, result);

        path.pop_back();
    }

};