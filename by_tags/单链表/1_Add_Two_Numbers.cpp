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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(-1);
        int carry = 0;
        ListNode *prev = &dummy;
        ListNode *pa = l1;
        ListNode *pb = l2;
        for(;pa != nullptr || pb != nullptr; pa = pa==nullptr ? nullptr : pa->next, pb = pb==nullptr ? nullptr : pb->next, prev = prev->next ){
            int ai = pa == nullptr ? 0 : pa->val;
            int bi = pb == nullptr ? 0 : pb->val;
            int s = ai + bi + carry;
            carry = 0;
            if(s>=10){
                s = s - 10;
                carry = 1;
            }
            prev->next = new ListNode(s);

        }
        if(carry>0)
            prev->next = new ListNode(1);
        return dummy.next;

    }
};