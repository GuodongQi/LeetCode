/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {

        for(Node* cur = head; cur != NULL;){
            Node* node = new Node(cur->val);
            node->next = cur->next;
            cur->next = node;
            cur = node->next;
        }


        for(Node* cur = head; cur != NULL;){
            if(cur->random != NULL){
                cur->next->random = cur->random->next;
            }
            cur = cur->next->next;
        }

        Node dummy(-1);
        for (Node* cur = head, *new_cur = &dummy;
            cur != NULL; ) {
            new_cur->next = cur->next;
            new_cur = new_cur->next;
            cur->next = cur->next->next;
            cur = cur->next;
        }

        return dummy.next;
    }
};