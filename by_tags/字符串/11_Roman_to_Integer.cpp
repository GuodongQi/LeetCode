class Solution {
public:
    int romanToInt(string s) {
        int head = 0;
        int base = 1000;
        int ans = 0;
        char a, b, c;
        while(s[head] == 'M'){
            ans += base;
            ++head;
        }
        base /= 10;
        while(base){
            if(base == 100){
                a = 'C';
                b = 'D';
                c = 'M';
            }
            else if(base == 10){
                a = 'X';
                b = 'L';
                c = 'C';
            }
            else{
                a = 'I';
                b = 'V';
                c = 'X';
            }
            cout << a << b << c << endl;
            if(head + 1 < s.size()){
                if(s[head] == a && s[head+1] == c){
                    ans += 9 * base;
                    head += 2;
                }
            }
            if(head + 1 < s.size()){
                if(s[head] == a && s[head+1] == b){
                        ans += 4 * base;
                        head += 2;
                    }
            }
            if(s[head] == b){
                ans += 5 * base;
                ++head;
            }
            while(s[head] == a){
                ans += base;
                ++head;
            }
            base /= 10;
        }
        return ans;
    }
};