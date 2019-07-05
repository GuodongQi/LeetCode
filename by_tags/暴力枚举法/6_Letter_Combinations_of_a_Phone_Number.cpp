class Solution {
public:
    const vector<string> keyboard { " ", "", "abc", "def", // '0','1','2',...
                                       "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

    vector<string> letterCombinations(string digits) {

        vector<string> res;
        string path;
        if(digits=="") return res;
        dfs(digits,0,0,path,res);
        return res;
    }


    void dfs(string digits, int start, int k, string &path, vector<string> &res ){
        if(path.size()==digits.size()){
            res.push_back(path);
            return;
        }
        for(int i = start; i<digits.size();i++){
            string tmp = keyboard[digits[i]-'0'];
            for(int j =k;j<tmp.size();j++){
                path.push_back(tmp[j]);
                dfs(digits, i+1,k, path,res);
                path.pop_back();
            }

        }
    }
};