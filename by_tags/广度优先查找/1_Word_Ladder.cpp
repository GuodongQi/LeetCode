class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(),wordList.end());
        if(!dict.count(endWord)) return 0;
        queue<string> q;
        q.push(beginWord);
        int res=0;
        while(!q.empty())
        {
            for(int layer=q.size();layer>0;layer--)
            {
                string word=q.front();q.pop();
                if(word == endWord) return res+1;
                for(int i=0;i<word.size();i++)
                {
                    string newWord=word;
                    for(char ch='a';ch<='z';ch++)
                    {
                        newWord[i]=ch;

                        if(dict.count(newWord) && newWord!=word)
                        {
                            q.push(newWord);
                            dict.erase(newWord);
                        }
                    }

                }
            }
            res++;
        }
        return 0;
    }
};