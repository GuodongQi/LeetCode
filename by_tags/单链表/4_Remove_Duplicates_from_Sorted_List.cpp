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
    ListNode* deleteDuplicates(ListNode* head) {

        if(head == nullptr) return head;

        int old_num = head->val;
        ListNode root(old_num - 1);
        ListNode* ptr = &root;

        ptr->next = head;
        head = head->next;
        ptr = ptr->next;

        while(head != nullptr){
            int new_num = head->val;
            if(old_num!=new_num){
                ptr->next = head;
                ptr = ptr->next;
            }
            head = head->next;
            old_num = new_num;
        }
        ptr->next = nullptr;
        return root.next;
    }
};