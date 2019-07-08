class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> path;
        vector<vector<int>> result;
        int start = 0;
        dfs(candidates, path, result, start, target);
        return result;
    }

    void dfs(vector<int> cand, vector<int> &path, vector<vector<int>> &result, int start, int target){
        if(target<0) return;
        if(target == 0){
            result.push_back(path);
            return;
        }

        for(int i = start; i<cand.size();i++){
            path.push_back(cand[i]);
            dfs(cand, path, result, i, target - cand[i]);
            path.pop_back();
        }

    }

};

sort后的
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());

        vector<int> path;
        vector<vector<int>> result;
        int start = 0;
        dfs(candidates, path, result, start, target);
        return result;
    }

    void dfs(vector<int> cand, vector<int> &path, vector<vector<int>> &result, int start, int target){
        if(target == 0){
            result.push_back(path);
            return;
        }

        for(int i = start; i<cand.size();i++){
            if (cand[i] > target) return;
            path.push_back(cand[i]);
            dfs(cand, path, result, i, target - cand[i]);
            path.pop_back();
        }

    }

};