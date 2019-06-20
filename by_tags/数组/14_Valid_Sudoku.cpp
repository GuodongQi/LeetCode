class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<char> nums;

        // for row
        for(int i=0; i<9;i++){
            nums={};
            for(int j=0; j<9;j++)
                nums.push_back(board[i][j]);
            if(!check(nums)) return false;

        }
        // for col
        for(int i=0; i<9;i++){
            nums={};
            for(int j=0; j<9;j++)
                nums.push_back(board[j][i]);
            if(!check(nums)) return false;

        }
        // for cell
        for(int i=0; i<3; i++)
            for(int j=0; j<3; j++){
                nums = {};
                for(int ii=0;ii<3;ii++)
                    for(int jj=0;jj<3;jj++)
                        nums.push_back(board[i*3+ii][j*3+jj]);
            if(!check(nums)) return false;
            }

    return true;

    }

    bool check(vector<char>&nums){
        unordered_map<char, bool> maps;
        for(auto c:nums){
            if(c!='.'){
                if(maps.find(c)!=maps.end())
                    return false;
                maps[c]=true;
            }
        }
        return true;
    }
};