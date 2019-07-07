class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;
        dfs(s,path,res,0,1);
        return res;
    }

    void dfs(string &s,  vector<string> &path, vector<vector<string>> &res, int left, int right){ // left right分别表示隔板
        if(right == s.size()){
            if(isPalindrome(s, left, right-1)){
                path.push_back(s.substr(left, right-left));
                res.push_back(path);
                path.pop_back();
            }
            return;
        }

        dfs(s, path, res, left, right+1); //断开

        if (isPalindrome(s, left, right - 1)) { //
            path.push_back(s.substr(left, right - left));
            dfs(s, path, res, right, right + 1);
            path.pop_back();
        }




    }



    bool isPalindrome(string &s, int start, int end) {
        while(start < end && s[start] == s[end]) {
            ++start;
            --end;
        }
        return start >= end;
    }

};