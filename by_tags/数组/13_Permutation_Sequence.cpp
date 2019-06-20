class Solution {
public:
    string getPermutation(int n, int k) {
        string result;
        unordered_map<int,bool> maps;
        for(int i = 1;i<=n;i++) maps[i]=false;
        k--;
        for(int i = n-1; i >= 0; i--){
            int fa = fact(i);
            int an = k / fa;
            k = k % fa;

            for(int j=1;j<=n;j++){
                if(!maps[j]) an--;
                if(an<0){
                     result.push_back(j+'0');
                     maps[j] = true;
                     break;
                }

            }

        }

        return result;
    }
