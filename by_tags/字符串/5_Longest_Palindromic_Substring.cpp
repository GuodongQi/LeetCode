class Solution {
public:
    string longestPalindrome(string s) {
        const int n = s.size();
        if(n==0) return "";
        bool f[n][n];
        fill_n(&f[0][0], n*n, false);

        int max_len = 1, start = 0;
        for(int i = 0; i < s.size(); i++){
            f[i][i] = true;
            for(int j = 0; j<i;j++){
                f[j][i] = (s[i] == s[j]&&(i -j <2 || f[j+1][i-1]));
                if(f[j][i] && max_len < i -j + 1){
                    max_len = i -j + 1;
                    start = j;
                }
            }
        }
        return s.substr(start, max_len);
    }
};