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
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode root(-1);
        ListNode* ptr = &root;
        ListNode* h = head;
        int length = 1;
        if(head==nullptr) return head;
        if(k==0) return head;
        while(head->next!=nullptr){
            head = head->next;
            length++;
        }
        ListNode* t = head;
        t->next = h;
        k = length - k % length;
        for(int i = 0; i<k; i++){
            h = h->next;
        }

        for(int i = 0; i<length; i++){
            ptr->next = h;
            ptr = ptr->next;
            h = h->next;

        }
        ptr->next = nullptr;
        return root.next;
    }
};