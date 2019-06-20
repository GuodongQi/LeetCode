class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int first_index = 0;
        int second_index = 0;
        for(int i = nums.size()-2; i>=0;i--){
            if(nums[i]< nums[i+1]) {first_index = i; break;}
        }


        for(int i = nums.size()-1; i>=0;i--){
            if(nums[i]> nums[first_index]) {second_index = i; break;}
        }
        // cout<<second_index<<first_index<<endl;
        // swap
        swap(nums, first_index, second_index);

        // reverse
        if(second_index==0) reverse(nums, first_index);
        else
        reverse(nums, first_index+1);

    }

    void swap(vector<int> &nums, int f_i, int s_i){
        int tmp = nums[f_i];
        nums[f_i] = nums[s_i];
        nums[s_i] = tmp;
    }

    void reverse(vector<int> &nums, int index){
        int i = index;
        int j = nums.size() - 1;
        while(i<j){
            swap(nums,i++,j--);
        }
    }

};