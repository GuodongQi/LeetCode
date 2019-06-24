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
    ListNode* partition(ListNode* head, int x) {
        ListNode less(-1);
        ListNode more(-1);
        ListNode* less_ptr = &less;
        ListNode* more_ptr = &more;
        ListNode* ptr = head;
        while(ptr != nullptr){
            if(ptr->val < x){
                less_ptr->next = ptr;
                less_ptr = less_ptr->next;
            }
            else{
                more_ptr->next = ptr;
                more_ptr = more_ptr->next;
            }
            ptr = ptr->next;
        }
        more_ptr->next = nullptr;
        less_ptr->next = more.next;
        return less.next;
    }
};