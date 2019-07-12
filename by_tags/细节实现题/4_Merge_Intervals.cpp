class Solution
{
    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals)
        {
            vector<vector<int>> result;
            if(intervals.empty()) return result;
            sort(intervals.begin(), intervals.end(),[](vector<int> &x, vector<int> &y){ return x[0]<y[0]; });

            vector<int> temporary = intervals[0];

            for(int i=1;i<intervals.size();i++)
            {
                if(temporary[1]< intervals[i][0])
                    {
                        result.push_back(temporary);
                        temporary=intervals[i];
                    }
                else
                    {
                        temporary[1]=max(temporary[1],intervals[i][1]);
                    }
            }
            result.push_back(temporary);
            return result;
        }
};