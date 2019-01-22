# LeetCode
1. [two_sum.py](./codes/1_two_sum.py)  
   * 创建一个字典，判断字典里是否含有target-nums[i]  
2. [add_two_nums.py](./codes/2_add_two_nums.py)  
   * 主要是对迭代器的考察  
3. [Longest_Substring_Without_Repeating_Characters.py](./codes/3_Longest_Substring_Without_Repeating_Characters.py)  
   * 定义滑动窗口，窗口内不需要再过一遍  
4. [Median_of_Two_Sorted_Arrays.py](./codes/4_Median_of_Two_Sorted_Arrays.py)  
   * 类似分治法对两个序列进行排序  
5. [Longest_Palindromic_Substring.py](./codes/5_Longest_Palindromic_Substring.py) 
   * 方法1：暴力循环，时间复杂度高 n^3
   * 方法2：反转序列，寻找s与s’相同的最大的序列组（暂未实现）
   * 方法3：动态规划，对方法1的改进，避免重复计算已经验证过的回文序列
6. [ZigZag_Conversion.py](./codes/6_ZigZag_Conversion.py)
   * 方法1：构建形如解释原因的矩阵，方法较慢
   * 方法2: 建立索引，对每个v字符的位置进行预先定义
7. [Reverse_Integer.py](./codes/7_Reverse_Integer.py)
   * 没啥意思，lazy的方法反而更快
8. [String_to_Integer.py](./codes/8_String_to_Integer.py)
   * 需要注意特殊情况，比如9-6这种。另外也可以使用.strip方法去除空格
