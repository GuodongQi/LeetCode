class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for(auto c : tokens){
            if(c != "+"&& c != "-"&& c != "*" && c != "/"){
                stk.push(stoi(c));
            }else {
                int num1 = stk.top();
                stk.pop();
                int num2 = stk.top();
                stk.pop();
                int ans = 0;
                if(c == "+")
                    ans = num1 + num2;
                else if(c == "-")
                    ans = num2 - num1;
                else if(c == "*")
                    ans = num2 * num1;
                else if(c == "/")
                    ans = num2 / num1;
                stk.push(ans);
            }
        }
        return stk.top();
    }
};