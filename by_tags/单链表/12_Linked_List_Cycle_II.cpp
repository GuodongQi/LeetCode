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
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while(fast&&fast->next){
            fast=fast->next->next;
            slow = slow->next;
            if(fast==slow){
                ListNode *ptr=head;
                while(ptr!=slow){
                    slow=slow->next;
                    ptr = ptr->next;
                }
                return ptr;
            }
        }
        return nullptr;
    }
 };



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
    ListNode reorderList(ListNode* head) {
        if(head == nullptr || head->next ==nullptr) return *head;

        ListNode *slow = head, *fast = head, *prev = nullptr;

        while(fast&&fast->next){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = nullptr;
        slow = reverse(slow);
        return *slow;
        //merge
        ListNode *cur = head;
        while(cur->next){
            ListNode *tmp = cur->next;
            cur->next = slow;
            cur->next->next = tmp;
            slow = slow->next;
            cur = tmp;
        }
        cur->next = slow;

        return *cur;

    }

    ListNode* reverse(ListNode* head){
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *prev = head;
        for(ListNode *cur = head->next,*next=cur->next;cur;){
            cur->next = prev;
            prev = cur;
            cur = next;
            next = next ? next->next : nullptr;
        }
        head->next = nullptr;
        return prev;
    }
};

