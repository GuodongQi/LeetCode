/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode root(-1);
        root.next = head;
        ListNode* ptr = &root;
        while(ptr!=nullptr && ptr->next!=nullptr && ptr->next->next!=nullptr){
            ListNode* pre = ptr;
            ListNode* cur = ptr->next;
            ListNode* next = cur->next;
            pre->next = next;
            cur->next = next->next;
            next->next = cur;
            ptr = ptr->next->next;

        }
        return root.next;
    }
};