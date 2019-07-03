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
15. <a name="shuzu15"></a>[Trapping_Rain_Water](by_tags/数组/15_Trapping_Rain_Water.cpp)
    * 对于每个柱子找到左右两边的最大最小值. 动态规划.
    * 使用stack
    * 理论上第二个方法会好,但实际运行的时候第一个方法运行时间是4ms,第二个方法的运行时间是8ms
16. [Rotate_Image](by_tags/数组/16_Rotate_Image.cpp)
    * 首先沿着中心线翻转，然后沿着主对角线翻转。
    * 或者首先沿河次对角线翻转，然后沿着中心线翻转。
17. [Plus_one](by_tags/数组/17_Plus_one.cpp)
    * c.begin() 返回一个迭代器，它指向容器c的第一个元素
    * c.end() 返回一个迭代器，它指向容器c的最后一个元素的下一个位置
    * c.rbegin() 返回一个逆序迭代器，它指向容器c的最后一个元素
    * c.rend() 返回一个逆序迭代器，它指向容器c的第一个元素前面的位置
18. [Climbing_Stairs](by_tags/数组/18_Climbing_Stairs.cpp)
    * 递归，太慢，采用迭代法
    * 利用通项公式，此方法最快。
19. [Gray_Code](by_tags/数组/19_Gray_Code.cpp)
    * 数学公式，见详解
    * 递归。先计算第n-1位的，然后镜像。(*it)[0]要这样加括号。
    * a<<n 将a的二进制数左移n位，右补0. 相当于2次方。
    * reserve是容器预留空间，但并不真正创建元素对象，在创建对象之前，不能引用容器内的元素，因此当加入新的元素时，需要用push_back()/insert()函数。
    * 说实话，第二个方法原理懂了，代码没看懂。
20. [Set_Matrix_Zeroes](by_tags/数组/20_Set_Matrix_Zeroes.cpp)
    * 要求空间复杂度在m+n之间。
    * 可以设置两个变量分别储存每一行或列是否含有0
    * 也可以只设置一个行和列变量，来判断是否有0
21. [Gas_Station](by_tags/数组/21_Gas_Station.cpp)
    * 如果所有的gas和大于所有的cost和，那么肯定能够走完。所以找两个值，一个储存所有路径的和，另一个储存某sum和大于0的索引
22. [Candy](by_tags/数组/22_Candy.cpp)
    * 主要是辨认最小值和极值点。这里需要关注极值大点以及步长而不是最小值点。
    * 第二个方法好理解。
23. [Single_Number](by_tags/数组/23_Single_Number.cpp) 
    * 使用hash map；
    * 使用异或；0与任何值异或都是0；
24. [Single_Number_II](by_tags/数组/24_Single_Number_II.cpp)
    * 异或的拓展。理解方式，创建一个循环方法，比如00->01->10(00)。
    第一位的变化规律0,1,0,0,1,0 中间0->0，当第二位是1时可以将其赋值为0，不使用异或。
    第二位的变化规律0,0,1,0,0,1 从0->0，因为事先计算好了第一位，所以当计算好的第一位是1时，可以不使用异或，直接赋值0；
      
## 单链表类
1. [Add_Two_Numbers](by_tags/单链表/1_Add_Two_Numbers.cpp)
    * 有几点需要注意的地方：？的使用。另外对于nullptr的判断，不需要再额外拉出来，如果是nullptr将其设为0即可
2. [Reverse_Linked_List_II](by_tags/单链表/2_Reverse_Linked_List_II.cpp) 
    * 头插法
3. [Partition_List](by_tags/单链表/3_Partition_List.cpp)
    * 两个指针，一个指针指向小的，另一个指针指向大的。
4. [Remove_Duplicates_from_Sorted_List](by_tags/单链表/4_Remove_Duplicates_from_Sorted_List.cpp)
    * 没啥好说的.参考代码里有delete，用来释放内存
5. [Remove_Duplicates_from_Sorted_List_II](by_tags/单链表/5_Remove_Duplicates_from_Sorted_List_II.cpp)
    * 初始化时。使用INT_MIN比较好
    * 使用delete来进行删除节点操作；
6. [rotate_list](by_tags/单链表/6_rotate_list.cpp)    
    * 头尾相连，然后循环
    * 最好不要在head上操作，参考代码中新的头和断开环的操作值得学习
7. [remove_nth_node_from_end_of_list](by_tags/单链表/7_remove_nth_node_from_end_of_list.cpp)
    * 答案很奇妙。两个指针，一起走；
8. [Swap_Nodes_in_Pairs](by_tags/单链表/8_Swap_Nodes_in_Pairs.cpp)
    * 关键是定义三个变量，一个是之前指针，一个是当前指针，一个是之后指针，然后进行交转。
9. [Reverse_Nodes_in_k_Group](by_tags/单链表/9_Reverse_Nodes_in_k_Group.cpp)
    * 翻转链表，就是相当于把链表的指针方向改一改；(使用三个指针，完成翻转后，head节点指向nullptr，返回的应该是pred指针)
10. [Copy_List_with_Random_Pointer](by_tags/单链表/10_Copy_List_with_Random_Pointer.cpp)
    * 两张表存在关系，就是每个节点先创建两次，然后拆分
11. [Linked_List_Cycle](by_tags/单链表/11_Linked_List_Cycle.cpp)
    * hash表
    * 两个指针，一个指针走的慢，一个指针走得快, 如果相遇，说明有环；
12. [Linked_List_Cycle_II](by_tags/单链表/12_Linked_List_Cycle_II.cpp)
    * 利用数学公式，解法很经典。
13. [Reorder_List](by_tags/单链表/13_Reorder_List.cpp)
    * 从中间分隔使用slow和fast的模式
    * 翻转操作，注意第31行，如果放在32行后面，将导致超时，因为32行有两个next
14. [LRU_Cache](by_tags/单链表/14_LRU_Cache.cpp)
    * 这一题我选择死亡

## 字符串

1. [Valid_Palindrome](by_tags/字符串/1_Valid_Palindrome.cpp)
    * transform 第1和2个参数是数据起始和结束位置（迭代器, 参数3是写入目标的起始位置,参数4是执行的操作（函数）
    * tolower() 将大写字母改写成小写字母
    * prev 主要指当前指针的前一个元素，常常和s.end搭配。
    * isalnum用来判断是不是字符和数字，如果是则返回1,否则返回0;
    * 另外while的判断语句还需要注意,left小于right,而不能是left!=right
2. [Implement_strStr](by_tags/字符串/2_Implement_strStr().cpp)
    * 暴力算法已经够了,o(m*n)时间复杂度,空间复杂度为1;
    * KMP算法,关于next的求法理解,请看https://blog.csdn.net/qq_37969433/article/details/82947411
3. [String_to_Integer](by_tags/字符串/3_String_to_Integer(atoi).cpp)
    * 细节题.略
4. [Add_Binary](by_tags/字符串/4_Add_Binary.cpp)   
    * result.insert(result.begin(), val + '0'); 头插入,另外也可以用reverse操作
5. [Longest_Palindromic_Substring](by_tags/字符串/5_Longest_Palindromic_Substring.cpp)
    * 动态规划的方法, fill_n函数的应用, substr 的应用
    * 了解Manacher's Algorithm的方法 https://segmentfault.com/a/1190000003914228
6. [Regular_Expression_Matching](by_tags/字符串/6_Regular_Expression_Matching.cpp)
    * 动态规划,多种情况讨论
7. [Wildcard_Matching](by_tags/字符串/7_Wildcard_Matching.cpp)
    * 和上一题类似,主要是遇到\*时,应该怎么做
8. [Longest_Common_Prefix](by_tags/字符串/8_Longest_Common_Prefix.cpp)
    * 纵向扫描 横向扫描 然后还可以分治法
9. [Valid_Number](by_tags/字符串/9_Valid_Number.cpp)
    * 细节题, 被称为最糟糕的题
10. [Integer_to_Roman](by_tags/字符串/10_Integer_to_Roman.cpp)
    * 把整数都列出来
11. [Roman_to_Integer](by_tags/字符串/11_Roman_to_Integer.cpp)
    * 和上一题类似
    * 从后往前,如果当前的字符比前面的字符小,说明应该是相减操作.
12. [Count_and_Say](by_tags/字符串/12_Count_and_Say.cpp)
    * 主要是题意的理解.
13. [Group_Anagrams](by_tags/字符串/13_Group_Anagrams.cpp)
    * 使用hash_map, 
    * 因为字母只有26个,所以可以使用26个key,每个value储存字母出现的次数.
14. [Simplify_Path](by_tags/字符串/14_Simplify_Path.cpp)
    * 可以使用find函数来简化. 另外关于vector转string, 可以使用stringstream定义变量,染红使用流输出;
15. [Length_of_Last_Word](by_tags/字符串/15_Length_of_Last_Word.cpp)
    * 偷懒,从后往前,找到第一个是字符的索引,然后,从这个索引再往前,找到第一个不是字符的索引,两个索引相减就对了.

## 栈
1. [Valid_Parentheses](by_tags/栈/1_Valid_Parentheses.cpp)
    * 典型先进先出
2. [Longest_Valid_Parentheses](by_tags/栈/2_Longest_Valid_Parentheses.cpp)
    * 动规
    * 两遍扫描,从左往右扫描一遍,然后从右扫描一遍
    * 使用栈,和上一题不同,这里因为只有小括号,所以可以储存(的索引值. 另外预先push一个-1,这样可以解决首字符是')'的问题;
    当遇到)时不管如何先弹出,如果弹出后stack为空,说明')'比'('多了,此时还应该push当前的索引. 如果弹出后stack不为空,说明有匹配,此时计算长度.
3. [Largest_Rectangle_in_Histogram](by_tags/栈/3_Largest_Rectangle_in_Histogram.cpp)
    * 和 数组类的第15题比较类似[这个](#shuzu15)
    * 在heights后push_back一个0;(以后理解))
4. [Evaluate_Reverse_Polish_Notation](by_tags/栈/4_Evaluate_Reverse_Polish_Notation.cpp)
    * 用stack完美解决

## 二叉树的遍历
1. [Binary_Tree_Preorder_Traversal](by_tags/树/二叉树的遍历/1_Binary_Tree_Preorder_Traversal.cpp)
    * stack,主要是morries遍历
2. [Binary_Tree_Inorder_Traversal](by_tags/树/二叉树的遍历/2_Binary_Tree_Inorder_Traversal.cpp)
    * 和1很相似
3. [Binary_Tree_Postorder_Traversal](by_tags/树/二叉树的遍历/3_Binary_Tree_Postorder_Traversal.cpp)
    * hard
4. [Binary_Tree_Level_Order_Traversal](by_tags/树/二叉树的遍历/4_Binary_Tree_Level_Order_Traversal.cpp)
    * 递归/迭代
5. [5_Binary_Tree_Level_Order_Traversal_II](by_tags/树/二叉树的遍历/5_Binary_Tree_Level_Order_Traversal_II.cpp)
    * 第四问的基础上, reserve一下result就好
6. [Binary_Tree_Zigzag_Level_Order_Traversal](by_tags/树/二叉树的遍历/6_Binary_Tree_Zigzag_Level_Order_Traversal.cpp)
    * 加一个left2right的flag
7. [Recover_Binary_Search_Tree](by_tags/树/二叉树的遍历/7_Recover_Binary_Search_Tree.cpp)
    * hard ,mirror遍历
8. [Same_Tree](by_tags/树/二叉树的遍历/8_Same_Tree.cpp)
    * easy 迭代或者遍历都可以
9. [Symmetric_Tree](by_tags/树/二叉树的遍历/9_Symmetric_Tree.cpp)    
    * 两个指针pq
10. [Balanced_Binary_Tree](by_tags/树/二叉树的遍历/10_Balanced_Binary_Tree.cpp)
    * 如果是平衡的,则返回高度,否则返回-1,递归.
11. [Flatten_Binary_Tree_to_Linked_List](by_tags/树/二叉树的遍历/11_Flatten_Binary_Tree_to_Linked_List.cpp)
    * 递归版本的好容易理解
12. ***

## 二叉树的构建
1. [Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal](by_tags/树/二叉树的构建/1_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.cpp)
    * 递归函数,从左往右
2. [Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal](by_tags/树/二叉树的构建/2_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.cpp)
    * go die
    
## 二叉查找树
1. [Unique_Binary_Search_Trees](by_tags/树/二叉查找树/1_Unique_Binary_Search_Trees.cpp)
    * 以i为根节点的二叉树,其左子树由[1...i-1]构成,右子树由[i+1...n]组成,所以可以推出其递归公式
2. [Unique_Binary_Search_Trees_II](by_tags/树/二叉查找树/2_Unique_Binary_Search_Trees_II.cpp)
    * 递归
3. [Validate_Binary_Search_Tree](by_tags/树/二叉查找树/3_Validate_Binary_Search_Tree.cpp)
    * 递归 注意函数的编写,三个参数,第一个参数传入节点的地址,第二个参数如果是左子树,那么就lower否则就upper
    * min max的传入方式
4. [Convert_Sorted_Array_to_Binary_Search_Tree](by_tags/树/二叉查找树/4_Convert_Sorted_Array_to_Binary_Search_Tree.cpp)
    * 递归, 二分法  
5. [Convert_Sorted_List_to_Binary_Search_Tree](by_tags/树/二叉查找树/6_Convert_Sorted_List_to_Binary_Search_Tree.cpp)
    * 因为给的是链表,所以不能随机访问,分治法
    
## 二叉树的递归

二叉树适合用递归,二叉树的先序中序后续可以看成DFS

1. [Minimum_Depth_of_Binary_Tree](by_tags/树/二叉树的递归/1_Minimum_Depth_of_Binary_Tree.cpp)
    * 使用递归, 输入两个参数,第一个参数是树的节点,第二个参数是是否有brother;
2. [Maximum_Depth_of_Binary_Tree](by_tags/树/二叉树的递归/2_Maximum_Depth_of_Binary_Tree.cpp)   
    * 和第一小问类似, 答案的解法更简洁
3. [Path_Sum](by_tags/树/二叉树的递归/3_Path_Sum.cpp)
    * 注意起始条件,特殊情况,当树为[] sum为0时,答案为false
4. [Path_Sum_II](by_tags/树/二叉树的递归/4_Path_Sum_II.cpp)
    * 递归,因为是个二位数组,所以要有个cur变量
5. [Binary_Tree_Maximum_Path_Sum](by_tags/树/二叉树的递归/5_Binary_Tree_Maximum_Path_Sum.cpp)
    * 难题,就像找到最大的连续序列和.
6. [Populating_Next_Right_Pointers_in_Each_Node](by_tags/树/二叉树的递归/6_Populating_Next_Right_Pointers_in_Each_Node.cpp)
    * 参考答案,不难,递归
7. [Sum_Root_to_Leaf_Numbers](by_tags/树/二叉树的递归/7_Sum_Root_to_Leaf_Numbers.cpp)
    * 第18 19 行的判断很关键