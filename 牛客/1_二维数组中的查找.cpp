class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int m = array.size();
        int n = array[0].size();
        int i = m - 1; int j = 0;
        while(i>=0 && j <n && j >=0 && i <m){
            if(target> array[i][j])
                j++;
            else if(target < array[i][j])
                i--;
            else
                return true;
        }
        return false;
    }
};