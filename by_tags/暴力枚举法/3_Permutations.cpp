class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        vector<int> path;
        dfs(nums, nums.begin(), path, res);
        return res;
    }

    void dfs(vector<int>& nums, vector<int>::iterator start, vector<int> &path, vector<vector<int>>& res){

        if(path.size() == nums.size()){
            res.push_back(path);
            return;
        }

        for(auto i :nums){
            auto pos = find(path.begin(), path.end(), i);
            if(pos == path.end()){
                path.push_back(i);
                dfs(nums,nums.begin(),path,res);
                path.pop_back();
            }
        }

    }
};
