class Solution {
public:
    vector<int> getRow(int numRows) {
        vector<int> cur;
        vector<int> prev;

        cur = vector<int>(1,1);
        if(numRows == 0) return cur;

//         cur = vector<int>(1,1);

//         if(numRows == 1) return cur;

        prev = cur;

        for(int i = 2; i<=numRows + 1; ++i){

           cur = vector<int>(i,1);

            for(int j = 1;j<i-1;++j){
                cur[j] = prev[j-1] + prev[j];
            }
            prev = cur;;
        }
        return cur;

    }
};