// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* p = head;
        ListNode* temp = nullptr;
        while (p->next != nullptr) {
            if (p->val == p->next->val) {
                temp = p->next;
                p->next = p->next->next;
                delete temp;
            }
            else 
                p = p->next;
        }
        return head;
    }
};
