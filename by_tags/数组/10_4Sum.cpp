class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if(nums.size()<3) return result;
        sort(nums.begin(),nums.end());
        for(int i=0; i < nums.size() - 3; i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            for( int j = i + 1;j< nums.size() - 2;j++){
                if(j > i + 1 && nums[j]==nums[j-1]) continue;
                int m = j + 1;
                int n = nums.size() - 1;
                while(m<n){
                    if(nums[i]+nums[j]+nums[m]+nums[n]>target){
                        n--;
                        while(nums[n]==nums[n+1] && m<n) n--;
                    } else if(nums[i]+nums[j]+nums[m]+nums[n]<target){
                        m++;
                        while(nums[m]==nums[m-1] && m<n) m++;
                    }else{
                        result.push_back({nums[i],nums[j],nums[m],nums[n]});
                        m++;
                        n--;
                        while(nums[m]==nums[m - 1] && m < n) m++;
                        while(nums[n]==nums[n + 1] && m < n) n--;
                    }

                }
            }

        }
        return result;

    }
};