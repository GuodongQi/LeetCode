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
9. [Palindrome_Number.py](./codes/9_Palindrome_Number.py)
   * 如果不转化成list，可以使用log函数来确定这个数的位数 divmod函数
10. [Regular_Expression_Matching.py](./codes/10_Regular_Expression_Matching.py)（果然有难度）
    * 使用动态规划方法，首先进行序列的补充，比如两个字符串同时添加相同的字符“0”后者“ ”，这样便于初始化
    * 对于 \* 的处理，如果 \*前的字符和指向s的字符相等时：例如 abbbbc 与 ab*c
       * 当\*表示0时，其真值和dp[i][j-2]相同
       * 当\*表示1时，其真值和dp[i][i-1]相同
       * 当\*表示多个时，其真值和dp[i-1][i]相同
    * 如果 \*前的字符和指向s的字符不相同时： 例如 abbbcbbbc 与 ab*c
       * \*只能表示0，其真值和dp[i][j-2]相同
11. [Container_With_Most_Water.py](./codes/11_Container_With_Most_Water.py) 
    * 方法一：暴力循环
    * 方法二：使用两个指针，一个指针指向最左，另一个指向最右，然后移动其中的较短的指针。
12. [Integer_to_Roman.py](./codes/12_Integer_to_Roman.py)
    * 建立一个罗马数字列表，
13. [Roman_to_Integer.py](./codes/13_Roman_to_Integer.py)
    * 同12
14. [Longest_Common_Prefix.py](./codes/14_Longest_Common_Prefix.py)
    * 暴力字符循环
    * 分治法
    * 二叉树法
15. [3Sum.py](./codes/15_3Sum.py)
    * 字典法
    * 三个指针方法
    * python 判断是否在列表中很费时间
16. [3Sum_Closest.py](./codes/16_3Sum_Closest.py)
    * 同15，使用三个指针的方法
