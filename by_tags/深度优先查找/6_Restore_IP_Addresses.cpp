class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        vector<string> path; // 存放中间的ip地址，这个思路特别好。
        int index = 0;
        dfs(s, path, result, index);
        return result;
    }

    void dfs(string &s, vector<string> &path, vector<string> & result, int index){

        if(path.size() == 4 && index == s.size()){
            result.push_back(path[0]+'.'+path[1]+'.'+path[2]+'.'+path[3]);
            return;
        }

        if(s.size()-index > (4-path.size())*3) return;
        if(s.size()-index < 4-path.size()) return;


        int num = 0;
       for(int i = index; i < index + 3; i++){
           num = num * 10 + (s[i] - '0');
           if(num<0 || num >255) continue;
           path.push_back(s.substr(index, i -index + 1));
           dfs(s, path, result, i + 1);
           path.pop_back();

           if(num == 0) break;
       }



    }
};