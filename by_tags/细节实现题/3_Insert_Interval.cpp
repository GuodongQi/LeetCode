class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        if(intervals.size()==0)
            return {newInterval};
        // 1. find index of interval strictly smaller or larger than newInterval
        int l=-1, r=intervals.size();
        for(int i=0; i<intervals.size(); i++) {
            if(intervals[i][1]<newInterval[0]) { l = i; }
            if(intervals[i][0]>newInterval[1]) { r = i; break;}
        }
        int s=intervals.size()-1;
        if(l<s) //works, AC
       // if(l<intervals.size()-1 && cout<<intervals.size()-1)// doesn't work, where the heck did (intervals.size()-1) go?
        {
            newInterval[0] = min(newInterval[0], intervals[l+1][0]);
        }
        if(r>0){
            newInterval[1] = max(newInterval[1], intervals[r-1][1]);
        }
        intervals.erase(intervals.begin()+l+1, intervals.begin()+r);
        intervals.insert(intervals.begin()+l+1, newInterval);

        return intervals;
    }
};