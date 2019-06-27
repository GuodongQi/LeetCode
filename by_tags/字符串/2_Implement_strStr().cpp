class Solution {
public:
    int strStr(string haystack, string needle) {

        int size = needle.size();
        int s = haystack.size();
        if(size == 0) return 0;
        vector<int> next(size, -1);
        int i = 0, j = -1;
        for(i = 1; i<size;i++){
            while(j>-1 && needle[j+1] != needle[i]) j = next[j];
            if(needle[i]==needle[j+1]) j++;
            next[i] = j;
        }
        // for(int i:next) cout<<i;

        j = -1;
        for(i = 0; i<s;i++){
            while(j>-1 && haystack[i]!=needle[j + 1]) j = next[j];
            if(haystack[i]==needle[j + 1]) j++;
            if(j == size - 1) return i - j;
        }

        return -1;
    }
};