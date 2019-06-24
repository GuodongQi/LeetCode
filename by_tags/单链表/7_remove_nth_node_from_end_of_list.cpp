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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode root(-1);
        ListNode* first = &root;
        ListNode* second = &root;
        int i = 0;
        while(first){
            first = first->next;
            if(i >= n){
                second = second->next;
            }
            i++;

        }
        //second->next = second->next->next;
        return root.next;
    }

};