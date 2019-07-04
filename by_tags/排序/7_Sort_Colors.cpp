class Solution {
public:
    void sortColors(vector<int>& A) {
        int red = 0, blue = A.size()-1;

        for(int i =0; i<blue + 1;){
            if(A[i] == 0)
                swap(A[i++], A[red++]);
            else if(A[i]==2)
                swap(A[i], A[blue--]);
            else
                i++;
        }

    }
};