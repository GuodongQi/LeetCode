class Solution {
public:
    vector<bool> col;
    vector<bool> main_diag;
    vector<bool> anti_diag;

    vector<vector<string>> solveNQueens(int n) {
        this->col = vector<bool>(n, false);
        this->main_diag = vector<bool>(2 * n - 1, false);
        this->anti_diag = vector<bool>(2 * n - 1, false);

        vector<vector<string>> res;
        vector<int> C(n, -1); //C[i] 表示第i行皇后所在的列编号
        dfs(C, res, 0);
        return res;

    }

    void dfs(vector<int> &C, vector<vector<string>> &res, int row){
        int N = C.size();

        if(row == N){ // 终止条件
            vector<string> solution;
            for(int i = 0; i<N; i++){
                string s(N, '.');
                for(int j = 0; j<N; j++){
                    if(j==C[i]) s[j] = 'Q';
                }
                solution.push_back(s);
            }
            res.push_back(solution);
            return;

        }

        for(int j = 0; j<N;j++){ // 一列一列的试
            const bool ok = !col[j] && !main_diag[row-j+N-1] && !anti_diag[row+j];
            if(!ok) continue; // 剪枝

            C[row] = j;
            col[j] = main_diag[row - j + N - 1] = anti_diag[row+j]=true;
            dfs(C, res, row+1);

            col[j] = main_diag[row-j+N -1] = anti_diag[row+j]=false;

        }

    }


};