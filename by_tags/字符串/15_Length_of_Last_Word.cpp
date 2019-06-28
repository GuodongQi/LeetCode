class Solution {
    public:
    int lengthOfLastWord(const string& s) {
        return lengthOfLastWord(s.c_str()); }
    private:
        int lengthOfLastWord(const char *s) {
            int len = 0;
            while (*s) {
                if (*s++ != ' ')
                    ++len;
                else if (*s && *s != ' ')
                    len = 0;
            }
            return len;
        }
};