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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr) return l2;
        if(l2 == nullptr) return l1;
        ListNode root(-1);
        ListNode* head = &root;
        while(l1 !=nullptr && l2!= nullptr){
            if(l1->val > l2->val){
                head->next = l2;
                l2 = l2->next;
            }else{
                head->next = l1;
                l1 = l1->next;
            }
            head = head->next;
        }
        head->next = l1 != nullptr ? l1:l2;
        return root.next;
    }
};