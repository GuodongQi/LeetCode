class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
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

        int prev = -1;
        for(int i = start; i< cand.size();i++){
            if (cand[i] > target) return;
            if(cand[i] == prev) continue;
            path.push_back(cand[i]);
            prev = cand[i];
            dfs(cand, path, result, i + 1, target - cand[i]);
            path.pop_back();
        }

    }
};