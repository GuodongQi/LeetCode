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

## 排序
1. [Merge_Sorted_Array](by_tags/排序/1_Merge_Sorted_Array.cpp)
    * 从后往前, 然后判断条件是nums1 nums2 的索引值是否大于0
2. [Merge_Two_Sorted_Lists](by_tags/排序/2_Merge_Two_Sorted_Lists.cpp)
    * 最后在赋值的时候,可以用?表达式,同时直接将下个节点复制到元节点,不用循环
3. [Merge_k_Sorted_Lists](by_tags/排序/3_Merge_k_Sorted_Lists.cpp)
    * 没啥好说的, 分治法就行了
4. [Insertion_Sort_List](by_tags/排序/4_Insertion_Sort_List.cpp)
    * 虽然演示是从后往前插入,但是还是要从前往后插入才行,因为这个没有前向列表.
    * debug 一脸蒙蔽...
5. [Sort_List](by_tags/排序/5_Sort_List.cpp)
    * 单链表适合规并排序,双链表适合快速排序.
6. [First_Missing_Positive](by_tags/排序/6_First_Missing_Positive.cpp)
    * 桶排序
7. [Sort_Colors](by_tags/排序/7_Sort_Colors.cpp)
    * 第一种方法,是统计 0 1 2 的个数,然后再遍历一遍写进去.
    * 第二种方法, 两个指针,一个是red 一个是blue,往中间走.

## 查找
1. [Search_for_a_Range](by_tags/查找/1_Search_for_a_Range.cpp)
    * 已经排好序,所以使用二分法.
    * 于是lower_bound 和 upper_bound的用法 
2. [Search_Insert_Position](by_tags/查找/2_Search_Insert_Position.cpp)
    * 就是实现lower_bound方法
3. [Search_a_2D_Matrix](by_tags/查找/3_Search_a_2D_Matrix.cpp) 
    * 二分法,可以在整个矩阵上进行二分,这样简单点

## 暴力枚举
1. [Subsets](by_tags/暴力枚举法/1_Subsets.cpp)
    * 递归的时候,要注意输入的参数, 4个, 其中一个还有子集的大小.
    * 还有迭代的方法,没看懂
2. [SubsetsII](by_tags/暴力枚举法/2_SubsetsII.cpp)
    * 递归,dfs,这个方法用在1上居然更快
3. [Permutations](by_tags/暴力枚举法/3_Permutations.cpp)
    * 关键是结束条件,在什么情况下,res可以推进path
    * 然后使用find函数
4. [Permutations](by_tags/暴力枚举法/4_PermutationsII.cpp)
    * 明天看 
5. [Combinations](by_tags/暴力枚举法/5_Combinations.cpp)
    * dfs
6. [Letter_Combinations_of_a_Phone_Number](by_tags/暴力枚举法/6_Letter_Combinations_of_a_Phone_Number.cpp)
    * dfs 第25行的第三个参数为什么是k而不是k+1需要好好揣摩.

## 广度优先查找
1. [Word_Ladder](by_tags/广度优先查找/1_Word_Ladder.cpp)
    * 使用一个queue hard
2. [Word_LadderII](by_tags/广度优先查找/2_Word_LadderII.cpp)
    * 我选择放弃
3. [Surrounded_Regions](by_tags/广度优先查找/3_Surrounded_Regions.cpp)
    * 先检查最外圈,然后把o设置成1,然后再依次检查内圈
#### 小结
广度优先查找不像深度优先查找,没有递归的本质. 一般都是求解最短最小的问题.
模板看pdf或者网上找(推荐).
1. [Palindrome_Partitioning](by_tags/深度优先查找/1_Palindrome_Partitioning.cpp)
    * 隔板法, 左边的第一个元素肯定会参与,不是那种求最长字串的那种
2. [Unique_Paths](by_tags/深度优先查找/2_Unique_Paths.cpp)
    * 深搜,也就是递归,会超时. 用动态规划会好点. 可以加个缓存,变成备忘录法
3. [Unique_PathsII](by_tags/深度优先查找/3_Unique_PathsII.cpp)
    * 当有障碍时,说明通向这条路的方法变成0,强制变成0就好.另外,dfs时,返回的类型设置为int 
    * 还是动态规划耗时短.
4. [4_N_queen](by_tags/深度优先查找/4_N_queen.cpp)
    * 三个缓存,主对角线,副对角线,以及一行 作为缓存
5. [5_N_QueenII](by_tags/深度优先查找/5_N_QueensII.cpp)
    * 和上一题对比起来就是不用输出每个结果,只输出结果的总数
6. [Restore_IP_Addresses](by_tags/深度优先查找/6_Restore_IP_Addresses.cpp)
    * 必须走到底,才能发现是不是有效的地址. 答案的path vector<string>值得参考
7. [Combination_Sum](by_tags/深度优先查找/7_Combination_Sum.cpp)
    * 略,简单. 相同的代码,别人可以faster than 70%,原因是因为先排序,中间在循环里有一步骤可以提前剪枝
8. [Combination_Sum_II](by_tags/深度优先查找/8_Combination_Sum_II.cpp)
    * 关于判断是不是重复, 不能用list\[i-1\]==list\[i\],因为可能会消掉\[1,1,2\]这种的答案,使用prev参数很好,参看答案.
9. [Generate_Parentheses](by_tags/深度优先查找/9_Generate_Parentheses.cpp)
    * 注意剪枝判断条件.
10. [Sudoku_Solver](by_tags/深度优先查找/10_Sudoku_Solver.cpp)
    * 在判断是否合法的时候,只判断ij处填充的数字是否合法就行,其他地方不用判断
11. [Word_Search](by_tags/深度优先查找/11_Word_Search.cpp)
    * 剪枝条件,  if (k == word.length() - 1) return true;  // found the last char
    * 另外还可以使用额外的参数,来储存是否使用.

## 分治法
1. [Pow(x,n)](by_tags/分治法/1_Pow(x,n).cpp)
    * 注意 int 和long的范围
2. [Sqrt(x)](by_tags/分治法/2_Sqrt(x).cpp)
    * 使用二分法要考虑的边界太多,使用牛顿法最好
    
## 贪心法
1. [Jump_Game](by_tags/贪心法/1_Jump_Game.cpp)
    * 还是用动态规划省心, 注意状态是指从0到终点所剩余的步数,这样才容易列状态方程.
2. [Jump_Game_II](by_tags/贪心法/2_Jump_Game_II.cpp)
    * 贪心, 用left,right表示当前步数能到的区间范围.
3. [Best_Time_to_Buy_and_Sell_Stock](by_tags/贪心法/3_Best_Time_to_Buy_and_Sell_Stock.cpp)
    * 贪心法, 最低点买入, 更新最低点
4. [Best_Time_to_Buy_and_Sell_Stock_II](by_tags/贪心法/4_Best_Time_to_Buy_and_Sell_Stock_II.cpp)
    * 贪心法, 只要后一天比前一天价格高,就可以买进卖出.
5. [Longest_Substring_Without_Repeating_Characters](by_tags/贪心法/5_Longest_Substring_Without_Repeating_Characters.cpp)
    * 涉及到字符串,因此可以设置数组,索引为字符串.
6. [Container_With_Most_Water](by_tags/贪心法/6_Container_With_Most_Water.cpp)
    * 使用两个指针, 面积只取决于最小短板,因此可以将比较两边短板,较小的短板移动

## 动态规划
1. [1_Triangle](by_tags/动态规划/1_Triangle.cpp)
    * 注意边界条件,另外也可以从后往前递归.
2. [Maximum_Subarray](by_tags/动态规划/2_Maximum_Subarray.cpp)
    * 开启一个数组用来储存前n项字串最大和,如果字串和大于零,说明有贡献,字串可以加上
3. [Palindrome_Partitioning_II](by_tags/动态规划/3_Palindrome_Partitioning_II.cpp)
    * i从0到n之间的回文,然后j从0到i,分别判断回文和递归公式.
4. [Maximal_Rectangle](by_tags/动态规划/4_Maximal_Rectangle.cpp)
    * 占个坑
5. [Best_Time_to_Buy_and_Sell_Stock_III](by_tags/动态规划/5_Best_Time_to_Buy_and_Sell_Stock_III.cpp)
    * pdf给的解析特别赞,分成两段.
6. [Interleaving_String](by_tags/动态规划/6_Interleaving_String.cpp)
    * pdf讲解的很好,一定要看看
7. [Scramble_String](by_tags/动态规划/7_Scramble_String.cpp)
    * 占坑
8. [Minimum_Path_Sum](by_tags/动态规划/8_Minimum_Path_Sum.cpp)
    * 常规的动态规划, 使用动态数组会简便点
9. [Edit_Distance](by_tags/动态规划/9_Edit_Distance.cpp)
    * 这题的关键是状态的确定. 设f\[i]\[j]为word1\[0:i] word\[0:j]之间的最小距离,此时便
    可以分成3种情况
        ** 如果c==d,说明不需要操作, 则f\[i]\[j] = f\[i-1]\[j-1]
        ** 如果c!=d,
            如果需要删除操作,c替换成d,则 f\[i]\[j]=f\[i-1]\[j-1]+1; 如果c后面增添,则说明 f\[i]\[j]=f\[i]\[j-1]+1; 如果c后面删除,则说明
            f\[i]\[j]=f\[i-1]\[j]+1
10. [Decode_Ways](by_tags/动态规划/10_Decode_Ways.cpp)
    * 类似菲波纳契数列,但是得对prev判断
11. [Distinct_Subsequences](by_tags/动态规划/11_Distinct_Subsequences.cpp)
    * 虽然标的是hard,但是掌握了套路就行.形如第9题,这样设置状态
12. [Word_Break](by_tags/动态规划/12_Word_Break.cpp)
    * dfs 或 动态规划
13. [Word_BreakII](by_tags/动态规划/13_Word_BreakII.cpp)
    * dfs 注意边界条件

## 图
1. [Clone_Graph](by_tags/图/1_Clone_Graph.cpp)
    * 图的遍历,dfs或者bfs. 用一个hash表储存节点,当节点存在时,说明已经copy过,无需要再copy,如果不存在则拷贝.

## 细节实现题
1. [Reverse_Integer](by_tags/细节实现题/1_Reverse_Integer.cpp)
    * 边界条件很恶心... longlong t = x , 然后注意不能使用t = -x,应该是 t=-t;
2. [Palindrome_Number](by_tags/细节实现题/2_Palindrome_Number.cpp)
    * 关键是 首位和末尾,如何取出,末尾好办,直接求余.首位需要计算位数d, 位数的计算,参考代码
3. [Insert_Interval](by_tags/细节实现题/3_Insert_Interval.cpp)
    * 通过比较 if(intervals[i][1]<newInterval[0]) { l = i; }
    if(intervals[i][0]>newInterval[1]) { r = i; break;}
    得到区间索引. 然后再次比较  
    newInterval[0] = min(newInterval[0], intervals[l+1][0]);
    newInterval[1] = max(newInterval[1], intervals[r-1][1])
    得到新的片段的应该是多少.
    然后使用intervals.erase 和 intervals.insert
4. [Merge_Intervals](by_tags/细节实现题/4_Merge_Intervals.cpp)
    * sort用法 sort(intervals.begin(), intervals.end(),[](vector<int> &x, vector<int> &y){ return x[0]<y[0]; });
    * 排序好后就简单了
5. [Minimum_Window_Substring](by_tags/细节实现题/5_Minimum_Window_Substring.cpp)
    * 创建两个数组,储存ascII码, 当遇到字符的时候,就加一.因为和字符顺序美观. 
    * 两个指针扫描,先扫描右   指针,直到符合了条件了,然后移动左指针.压缩到最小.
    * 两外leetcode提供的方法2可以看看.创建一个字典,索引为字符的位置,值为该字符.    
6. [Multiply_Strings](by_tags/细节实现题/6_Multiply_Strings.cpp)
    * 如果a是n位,b是m位,则乘积最多为n+m位
    * a的第2位诚意b的时候,结果在2+i位,另外注意进位.
    *因为将结果设为string,所以可以使用substr()
7. [Substring_with_Concatenation_of_All_Words](by_tags/细节实现题/7_Substring_with_Concatenation_of_All_Words.cpp)
    * hash map 的应用
8. [Pascal's_Triangle](by_tags/细节实现题/8_Pascal's_Triangle.cpp)
    * 左右两遍全插入1,然后动态规划.
9. [Pascal's_TriangleII](by_tags/细节实现题/9_Pascal's_Triangle_II.cpp)
    * 和上一题类似. 滚动数组可以了解.
10. [Spiral_Matrix](by_tags/细节实现题/10_Spiral_Matrix.cpp)
    * 看答案
11. [Spiral_Matrix_II](by_tags/细节实现题/11_Spiral_Matrix_II.cpp)
    * 和上一题一样.关键是先生成matrix
12. [Zig_Zag_Conversion](by_tags/细节实现题/12_Zig_Zag_Conversion.cpp)
    * 找规律,面试不可能出现
13. [Divide_Two_Integers](by_tags/细节实现题/13_Divide_Two_Integers.cpp)
    * 使用位运算翻倍, 边界条件.使用long
14. [Text_Justification](by_tags/细节实现题/14_Text_Justification.cpp)
    * For each line, I first figure out which words can fit in. According to the code, these words are words[i] through words[i+k-1]. Then spaces are added between the words. The trick here is to use mod operation to manage the spaces that can't be evenly distrubuted: the first (L-l) % (k-1) gaps acquire an additional space.
15. [Max_Points_on_a_Line](by_tags/细节实现题/15_Max_Points_on_a_Line.cpp)
    * 遍历每个点，得到这个点与其他点斜率，并保存到solpeMap中，斜率为键，值为个数,//并为每个solpeMap定义一个变量，保存这个map中值最大的值(maxCount)，每次加入map时更新这个最大值, 每次到solpeMap的最后用maxCount更新res;


## 语法总结 
1. f[m][n]数组填充方法 <br>
    `fill_n(&f[0][0], m*n, 0);`
2. 多个vector初始化 <br>
    vector(m, vector<int>(n, 0 ))       <br>
    vector<bool> row(m, false);        <br>
    vector<vector<int> > matrix(n, vector<int>(n)); 
3. vector 转 unordered_set <br>
  `unordered_set<string> dict(wordList.begin(),wordList.end());`
4. sort高级用法<br>
   `sort(intervals.begin(), intervals.end(),[](vector<int> &x, vector<int> &y){ return x[0]<y[0]; });`
  
       