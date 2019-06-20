class Solution{
public:
    bool search(vector<int>& nums, int target) {
        int first = 0, last = nums.size() - 1;

        while(last >= first){
            int tmp = 0;
            const int mid = first + (last - first) / 2;
            if(nums[mid] == target){return true;}

            if(nums[mid ] > nums[first]){

                if(nums[mid] > target && nums[first] <= target)
                    last = mid - 1 ;
                else
                    first = mid  + 1;
            }
            else if(nums[mid ] < nums[first]){
                if(nums[mid] < target && nums[last] >= target)
                    first = mid + 1;
                else
                    last = mid - 1;
             }
            else first++;
             }
        return false;
    }

};