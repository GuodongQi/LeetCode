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
                f[0][j] = f[0][j-2];
            }else{
                f[0][j] = false;
            }
        }


        for(int i = 1; i<m; i++){
           for(int j = 1; j <n; j++){
               if(p[j]=='*'){

                   if(s[i]==p[j-1] || p[j-1] == '.'){

                        f[i][j] = (f[i][j-1] || f[i][j-2] || f[i-1][j]);

                   }

                   else
                       f[i][j] = f[i][j-2];
               }else if(p[j]=='.'){
                   f[i][j] = f[i-1][j-1];
               }else{
                   f[i][j] = f[i-1][j-1] && s[i]==p[j];
               }
           cout<<f[i][j];

            }
            cout<<endl;
        }
        return f[m-1][n-1];

    }
};