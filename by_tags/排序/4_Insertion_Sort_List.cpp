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
    ListNode* insertionSortList(ListNode* head) {
        ListNode root(INT_MIN);
        ListNode *node = head;

        while(node!=nullptr){
            ListNode* pos = findPos(&root, node->val);
            ListNode* tmp = node->next;
            node->next = pos->next;
            pos->next = node;
            node = tmp;

            // for(auto t = &root; t!=nullptr; t = t->next)
            //    cout<<t->val<<" ";
            // cout<<endl;
        }

    return root.next;

    }

    ListNode* findPos(ListNode* head, int num){
        ListNode *curr, *prev;
        curr = head;
        prev = nullptr;
        while(curr != nullptr && curr->val <=num){
                prev = curr;
                curr = curr->next;
        }

        return prev;
    }

};