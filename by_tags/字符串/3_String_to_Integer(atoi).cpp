class Solution {
public:
    int myAtoi(string str) {
       bool negative = false;
       int result = 0 ;
       int i;
       for (i = 0; i < str.length(); i++){
           if (str[i] != ' ')
               break;
       }

       if ((str[i] < 48) || (str[i] > 57)){
           if (str[i] == '-'){
               if (str[i+1] > 47 && str[i+1] < 58){
                   i++;
                   negative = true;
               }
               else
                   return 0;
           } else if (str[i] == '+'){
               if (str[i+1] > 47 && str[i+1] < 58)
                   i++;
               else
                   return 0;
           } else
                   return 0;
       }

       while (str[i] > 47 && str[i] < 58){
           int digit = str[i] - 48;
           if (result < INT_MAX/10)
               result = result * 10 + digit;
           else if (result == INT_MAX/10){
               if (negative && digit > 7)
                   return INT_MIN;
               else if (!negative && digit > 6)
                   return INT_MAX;
               else
                   result = result * 10 + digit;
           }
           else{
               if (negative)
                   return INT_MIN;
               else if (!negative)
                   return INT_MAX;
           }
           i++;
        }

        if (negative) return -result;
        else return result;
    }
};