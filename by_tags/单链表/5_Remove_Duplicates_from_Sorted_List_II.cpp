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

        ListNode root(INT_MIN);
        ListNode* ptr = &root;
        bool duplicate = false;

        while(head != nullptr){
            duplicate = false;
            while(head->next != nullptr && head->val == head->next->val){
                duplicate = true;
                ListNode* tmp = head;
                head = head->next;
                delete tmp;
            }
            if(duplicate){
                ListNode* tmp = head;
                head = head->next;
                delete tmp;
                continue;

            }

            ptr->next = head;
            head = head->next;
            ptr = ptr->next;
        }

        ptr->next = head;
        return root.next;
    }
};