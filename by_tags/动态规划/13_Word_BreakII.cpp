class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {

        unordered_set dict(wordDict.begin(), wordDict.end());
        vector<vector<bool> > prev(s.length() + 1, vector<bool>(s.length()));
        vector<bool> f(s.length()+1, false);
        f[0] = true;
        for(int  i = 1; i <= s.length();++i){
            for(int j = i-1; j>=0; --j){
                if(f[i] &&dict.find(s.substr(j, i-j))!=dict.end()){
                    f[i] = true;
                    prev[i][j] = true;
                }
            }
        }

        vector<string>result;
        vector<string>path;

        gen_path(s,prev,s.length(),path,result);

        return result;
    }


    void gen_path(string &s, vector<vector<bool>> &prev, int cur, vector<string>&path, vector<string>&result){
            if(cur == 0){
                string tmp;
                for (auto iter = path.crbegin(); iter != path.crend(); ++iter)
                    tmp += *iter + " ";
                tmp.erase(tmp.end() - 1);
                result.push_back(tmp);

            }
            for (size_t i = 0; i < s.size(); ++i) {
                if (prev[cur][i]) {
                    path.push_back(s.substr(i, cur - i));
                    gen_path(s, prev, i, path, result);
                    path.pop_back();
                }
            }


        }



};