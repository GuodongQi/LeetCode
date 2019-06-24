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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode root(-1);
        root.next = head;

        ListNode *ptr = &root;
        for(int i = 0; i < m - 1; i++)
            ptr = ptr->next;
        ListNode* const head2 = ptr;

        ptr = head2->next;
        ListNode* cur = ptr->next;
        for(int i = m; i < n; i++){
            ptr->next = cur->next;
            cur->next = head2->next;
            head2->next = cur;
            cur = ptr->next;
        }

        return root.next;

    }
};