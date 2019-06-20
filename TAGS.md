# 数组类
1. [Remove_Duplicates_from_Sorted_Array](by_tags/数组/1_Remove_Duplicates_from_Sorted_Array.cpp)
    * 两个指针 一个指针用于表示不同数的数量，同时更新原序列。另一个指针用于遍历数组。
    * 使用STL的unique()和distance()函数
2. [Remove_Duplicates_from_Sorted_Array_II](by_tags/数组/2_Remove_Duplicates_from_Sorted_Array_II.cpp)
    * 加入一个变量来记录出现的次数，如果是没有排好序的，则用hash来储存次数
    * 也可以用 nums[i] == nums[i - 1] && nums[i] == nums[i + 1]
3. [Search_in_Rotated_Sorted_Array](by_tags/数组/3_Search_in_Rotated_Sorted_Array.cpp)     
    * 二分查找，关键在于边界的确定。另外还有判断条件的等号，一定不能忽略。
4. [Search_in_Rotated_Sorted_Array_II](by_tags/数组/4_Search_in_Rotated_Sorted_Array_II.cpp)
    * 形如[1,3,1,1,1]这种类型，只需要first++就行了，答案厉害
5. [Median_of_Two_Sorted_Arrays](by_tags/数组/5_Median_of_Two_Sorted_Arrays.cpp)    
    * 比较中心的位置（hard，代码待完善）
6. [Longest_Consecutive_Sequence](by_tags/数组/6_Longest_Consecutive_Sequence.cpp)
    * 如果不是要求o（n）的话，可以先排序在做，这样是o（nlogn）的复杂度。但是这里要求哦o(n)所以直接想到的就是使用哈希表。
    * 用一个unordered_map<int, bool> used来表示，进行左右扩充。
    * c++ 11的特性 for(auto i:nums) cout<<i; map.find 通过给定主键查找元素,没找到：返回unordered_map::end
7. [Two_Sum](by_tags/数组/7_Two_Sum.cpp)
    * 使用hash map来解决。
    * 暴力循环
    * 先排序，然后左右夹逼。排序算法o(n log n), 夹逼n。
8. [3Sum](by_tags/数组/8_3Sum.cpp)
    * 先排序，然后夹逼。时间复杂度0（n²）
9. [3Sum_Closest](by_tags/数组/9_3Sum_Closest.cpp)
    * 先排序，然后夹逼。因为所求的是和，所以不用检测是不是重复。这个还是都咬走一遍，注意gap的初始化。
10. [4Sum](by_tags/数组/10_4Sum.cpp)  
    * 县排序后夹逼，时间复杂度n三次方。会超时。 
    * 先储存两个数之和为hash表，然后两个变量c d。注意pair和make_pair的应用
11. [Remove_Element](by_tags/数组/11_Remove_Element.cpp)
    * 和第一题类似，使用一个index表示不同的数的位置
12. [Next_Permutation](by_tags/数组/12_Next_Permutation.cpp)
    * 答案方法奇妙。建议多看看 
13. [Permutation_Sequence](by_tags/数组/13_Permutation_Sequence.cpp) 
    * 利用12，暴力枚举，求得第1,2，。。。，k个序列。
    * 康拓编码的思路，见pdf，或者[这个博客](https://www.cnblogs.com/lucio_yz/p/5221772.html)  
    另外关于判断最小的n个（不出现）数中，采取hash表，具体看代码（这也是创新了吧）
14. [Valid_Sudoku](by_tags/数组/14_Valid_Sudoku.cpp)
    * 每一行，每一列，每个cell都进行检测
15. [Trapping_Rain_Water](by_tags/数组/15_Trapping_Rain_Water.cpp)
    *     

## 数组类
1. 2 