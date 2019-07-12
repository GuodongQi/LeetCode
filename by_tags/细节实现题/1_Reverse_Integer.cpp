class Solution {
public:
    int reverse(int x) {
        bool is_neg = false;

        long long r = 0;
        long long t = x;
        if(x<0){
            t = -t;
            is_neg = true;
        }

        for(; t; t/=10){
            r = r * 10 + t%10;
        }

        if (r > 2147483647 || (is_neg && r > 2147483648)) {
            return 0;
        }else if(is_neg){
            return -r;
        }else return r;

    }
};