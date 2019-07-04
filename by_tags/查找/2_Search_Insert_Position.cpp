class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      return distance(nums.begin(), lower_bound(nums.begin(),nums.end(),target));
    }

    template<typename Forward, typename T>

    Forward lower_bound(Forward first, Forward last, T value){
        while(first!=last){
            auto mid = next(first, distance(first, last)/2);
            if(value > *mid) first = ++mid;
            else last = mid;
        }
        return first;
    }
};