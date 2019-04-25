# LeetCode
1. [two_sum.py](./codes_1-50/1_two_sum.py)  
   * 创建一个字典，判断字典里是否含有target-nums\[i]  
2. [add_two_nums.py](./codes_1-50_1-50/2_add_two_nums.py)  
   * 主要是对迭代器的考察  
3. [Longest_Substring_Without_Repeating_Characters.py](./codes_1-50_1-50/3_Longest_Substring_Without_Repeating_Characters.py)  
   * 定义滑动窗口，窗口内不需要再过一遍  
4. [Median_of_Two_Sorted_Arrays.py](./codes_1-50_1-50/4_Median_of_Two_Sorted_Arrays.py)  
   * 类似分治法对两个序列进行排序  
5. [Longest_Palindromic_Substring.py](./codes_1-50_1-50/5_Longest_Palindromic_Substring.py) 
   * 方法1：暴力循环，时间复杂度高 n^3
   * 方法2：反转序列，寻找s与s’相同的最大的序列组（暂未实现）
   * 方法3：动态规划，对方法1的改进，避免重复计算已经验证过的回文序列
6. [ZigZag_Conversion.py](./codes_1-50_1-50/6_ZigZag_Conversion.py)
   * 方法1：构建形如解释原因的矩阵，方法较慢
   * 方法2: 建立索引，对每个v字符的位置进行预先定义
7. [Reverse_Integer.py](./codes_1-50_1-50/7_Reverse_Integer.py)
   * 没啥意思，lazy的方法反而更快
8. [String_to_Integer.py](./codes_1-50_1-50/8_String_to_Integer.py)
   * 需要注意特殊情况，比如9-6这种。另外也可以使用.strip方法去除空格
9. [Palindrome_Number.py](./codes_1-50_1-50/9_Palindrome_Number.py)
   * 如果不转化成list，可以使用log函数来确定这个数的位数 divmod函数
10. [Regular_Expression_Matching.py](./codes_1-50_1-50/10_Regular_Expression_Matching.py)（果然有难度）
    * 使用动态规划方法，首先进行序列的补充，比如两个字符串同时添加相同的字符“0”后者“ ”，这样便于初始化
    * 对于 \* 的处理，如果 \*前的字符和指向s的字符相等时：例如 abbbbc 与 ab*c
       * 当\*表示0时，其真值和dp\[i]\[j-2]相同
       * 当\*表示1时，其真值和dp\[i]\[i-1]相同
       * 当\*表示多个时，其真值和dp\[i-1]\[i]相同
    * 如果 \*前的字符和指向s的字符不相同时： 例如 abbbcbbbc 与 ab*c
       * \*只能表示0，其真值和dp\[i]\[j-2]相同
11. [Container_With_Most_Water.py](./codes_1-50_1-50/11_Container_With_Most_Water.py) 
    * 方法一：暴力循环
    * 方法二：使用两个指针，一个指针指向最左，另一个指向最右，然后移动其中的较短的指针。
12. [Integer_to_Roman.py](./codes_1-50_1-50/12_Integer_to_Roman.py)
    * 建立一个罗马数字列表，
13. [Roman_to_Integer.py](./codes_1-50_1-50/13_Roman_to_Integer.py)
    * 同12
14. [Longest_Common_Prefix.py](./codes_1-50_1-50/14_Longest_Common_Prefix.py)
    * 暴力字符循环
    * 分治法
    * 二叉树法
15. [3Sum.py](./codes_1-50_1-50/15_3Sum.py)
    * 字典法
    * 三个指针方法
    * python 判断是否在列表中很费时间
16. [3Sum_Closest.py](./codes_1-50_1-50/16_3Sum_Closest.py)
    * 同15，使用三个指针的方法
17. [Letter_Combinations_of_a_Phone_Number.py](./codes_1-50_1-50/17_Letter_Combinations_of_a_Phone_Number.py)
    * 没什么好说的，我用循环居然faster 100%
18. [4Sum.py](./codes_1-50/18_4Sum.py)
    * 可以在15的基础上做, 排名第一的方法f复杂度和我相同，但它只需79ms，向不清楚原因，估计是过早的sop的原因节省了很多时间
19. [Remove_Nth_Node_From_End_of_List](./codes_1-50/19_Remove_Nth_Node_From_End_of_List.py)
    * 自己创建一个根结点，这样可以避免讨论很多中情况，要学会利用这一点思想。第10题就是
    * 第二个方法比较巧妙。两个指针，第一个指针先走n步，这样剩余月要走的步数就是第二个指针要走的步数，然后再n出截断
20. [Valid_Parentheses](./codes_1-50/20_Valid_Parentheses.py)
    * 构建字典,使用堆栈，先进后出
21. [Merge_Two_Sorted_Lists](./codes_1-50/21_Merge_Two_Sorted_Lists.py) 
    * 使用递归的方法或迭代的方法   
22. [Generate_Parentheses](./codes_1-50/22_Generate_Parentheses.py)
    * 递归方法，应该重点掌握
23. [Merge_k_Sorted_Lists](./codes_1-50/23_Merge_k_Sorted_Lists.py)
    * 暴力循环
    * 分治法
    * one by one 合并
    * 使用优先级队列
    * 将所有的数变成一维list，然后sorted函数
24. [Swap_Nodes_in_Pairs](./codes_1-50/24_Swap_Nodes_in_Pairs.py)
    * pre->a->b->b.next 变成 pre->b->a->b.next
    最好是列出这个式子
25. [Reverse_Nodes_in_k](./codes_1-50/25_Reverse_Nodes_in_k-Group.py)
    * 截取前k个listnode，对每组的lkistnode进行反转
    * 其他方法导师再看县展坑
26. [Remove_Duplicates_from_Sorted_Array](./codes_1-50/26_Remove_Duplicates_from_Sorted_Array.py)
    * 简单体没什么好说的，注意看两种方法，答案那种方法号
27. [Remove_Element](./codes_1-50/27_Remove_Element.py)
    * 同上，使用两指针方法
28. [Implement_strStr](./codes_1-50/28_Implement_strStr().py)
    * easy题，没啥好说的，看方法二，太优秀了
29. [Divide_Two_Integers](./codes_1-50/29_Divide_Two_Integers.py) 
    * 主要是使用移位的方法，然后每次相减大于零时，说明还可以移位   
30. [Substring_with_Concatenation_of_All_Words](./codes_1-50/30_Substring_with_Concatenation_of_All_Words.py)
    * 方法一：使用两个字典，第一个字典储存words，其中key是word，value是word的出现次数。然后计算每个子字符串，字符串长度为word的长度
    每个子字符串中word的次数如果和dict1的value相同，则说明符合
    * 方法二：
31. [Next_Permutation](./codes_1-50/31_Next_Permutation.py)
    * 答案真是太奇妙了，看动图吧
32. [Longest_Valid_Parentheses](./codes_1-50/32_Longest_Valid_Parentheses.py)
    * brute force: two points, from every left to right judge whether valid
    * Using Dynamic Programming:  too hard. We make use of a dp array where ith element of dp represents the length of the longest valid substring ending at ith index.
    * Using Stack: hard
    * two counters left and right, easy: Two traversals of the string
33. [Search_in_Rotated_Sorted_Array](./codes_1-50/33_Search_in_Rotated_Sorted_Array.py)
    * binary search 
    * can find the index of min num
34. [Find_First_and_Last_Position_of_Element_in_Sorted_Array](codes_1-50/34_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py)
    * firstly find the first index, if nums[mid] == target, we should assign right = mid - 1 and in the meanwhile, we should write the mid index, then we use the same method to find the right target
35. [Search_Insert_Position](codes_1-50/35_Search_Insert_Position.py)
    * bruce force
    * binary search 
36. [Valid_Sudoku](codes_1-50/36_Valid_Sudoku.py)
    * the key is create a list to store number
38. [38_Count_and_Say](./codes_1-50/38_Count_and_Say.py)
    * easy, bruce force
39. [Combination_Sum](codes_1-50/39_Combination_Sum.py)
    * recursion: slow and not easy to delete duplication
    * backtracking example
40. [Combination_Sum_II](codes_1-50/40_Combination_Sum_II.py)
    * dfs condition, if j > 0 or if j > index are different
41. [First_Missing_Positive](codes_1-50/41_First_Missing_Positive.py)
    * the key is swap: 
    <br>  tmp = nums\[i] 
    <br>  nums\[i] = nums\[tmp - 1] 
    <br>  nums\[tmp - 1] = tmp
42. [Trapping_Rain_Water](./codes_1-50/42_Trapping_Rain_Water.py)
    * two points(my method, and range for maxheight. time limits: maxheight * width / 2 should range maxheight
    * brute force: for one height, find max and min height around it, and then, ans += min(left_max,right_max)-it
    * dynamic programming: store max of left and min height
    * stack:(not understand yet) we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water.
    * two points: if left_max < right_max the move left, else move right
43. [Multiply_Strings](./codes_1-50/43_Multiply_Strings.py)
    * understanding mul ,just like int
45. [Jump_Game_II](./codes_1-50/45_Jump_Game_II.py)
    * dynamic programming is running out of mem
    * BFS
46. [Permutations](./codes_1-50/46_Permutations.py)
    * same as 47
47. [Permutations_II](./codes_1-50/47_Permutations_II.py)
    * use dict keys to reduce duplicate
    * other method to be, the line "break" is beautiful 
48. [Rotate_Image](./codes_1-50/48_Rotate_Image.py)
    * ~i = -i - 1  often used in List 
    * zip method and zip(*) method 
    * reverse() method
49. [Categorize_by_Sorted_String](./codes_1-50/49_Categorize_by_Sorted_String.py)
    * 方法一：遍历，对每个单词进行排序，然后对比 
    * 方法二：每个字母对应一个数字，设置26个空格，如果有字母a，则在0出加一，最后比较有多少个是完全一样的
    * using dict.setdefault method 
50. [Pow[x, n]](./codes_1-50/50_Pow_x_n.py)
    * 使用递归实现
