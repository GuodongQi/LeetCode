class Solution {
    public:
    int numDistinct(const string &S, const string &T) {
        vector<long> f(T.size() + 1);
        f[0] = 1;
        for (long i = 0; i < S.size(); ++i) {
            for (long j = T.size() - 1; j >= 0; --j) {
                f[j + 1] += S[i] == T[j] ? f[j] : 0;
            }
        }
        return f[T.size()];
    }
};