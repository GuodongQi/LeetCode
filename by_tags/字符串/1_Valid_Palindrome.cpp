class Solution {
public:
    bool isPalindrome(string s) {
        // if(s=="") return true;
       transform(s.begin(), s.end(), s.begin(),::tolower);
        auto left = s.begin(), right = prev(s.end());
        while(left<right){
            if(!::isalnum(*left)) ++left;
            else if(!::isalnum(*right)) --right;
            else if(*left != *right) return false;
            else if(*left == *right){
                left++;
                right--;
            }

        }
        return true;
    }
};