class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> maps;
        vector<int> index;
        for(int i=0; i<nums.size();i++) maps[nums[i]] = i;
        for(int i=0; i<nums.size();i++){
            int tar = target - nums[i];
            if(maps.find(tar) != maps.end() && maps[tar]> i){
                index.push_back(i);
                index.push_back(maps[tar]);
                break;
            }

        }
        return index;

    }
};