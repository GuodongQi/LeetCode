class Solution {
public:
    bool isMatch(string s, string p) {
        s.insert(s.begin(),'0');
        p.insert(p.begin(),'0');

        const int m = s.size(), n = p.size();
        bool f[m][n];
        fill_n(&f[0][0], m*n, false);
        f[0][0] = true;


        for(int j = 1; j<n; j++){
            if(p[j] == '*'){
                f[0][j] = f[0][j-1];
            }else{
                f[0][j] = false;
            }
            // cout<<f[0][j];
        }
        // cout<<endl;

        for(int i = 1; i<m; i++){
           for(int j = 1; j <n; j++){
               if(p[j]=='*'){
                    f[i][j] = f[i-1][j] || f[i][j-1];
               }else if(p[j]=='?'){
                   f[i][j] = f[i-1][j-1];
               }else{
                    f[i][j] = f[i-1][j-1] && s[i]==p[j] ;
               }
           // cout<<f[i][j];

            }
            // cout<<endl;
        }
        return f[m-1][n-1];

    }
};