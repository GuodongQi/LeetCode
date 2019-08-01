class Solution {
public:
	void replaceSpace(char *str,int length) {
        int backspace = 0;
        for(int i = 0; i < length; i++){
            if(str[i] == ' ')
                backspace++;
        }

        int first = length - 1;
        int second = length + 2 * backspace - 1;
        for(;first>=0;first--){
            if(str[first]!=' '){
                str[second--] = str[first];
            }else{
                str[second--] = '0';
                str[second--] = '2';
                str[second--] = '%';
            }
        }

	}
};