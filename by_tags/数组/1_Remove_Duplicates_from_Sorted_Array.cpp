class Solution1 {
public:
    int removeDuplicates(vector<int>& nums) {
        int index=0, occr = 1;
        if(nums.empty()) return 0;

        for(int i = 1; i < nums.size(); i++){

            if(nums[index] != nums[i]){
                occr = 1;
                nums[++index] = nums[i];
            }else if(occr < 2){
                occr++;
                nums[++index] = nums[i];
            }
        }
        return index + 1;

    }
};



