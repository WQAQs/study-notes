## 1. 递归
## Time Complexity: O(n*k)
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    def reverse(head,tail):
        cur = head
        pre = None
        while cur != tail:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    if head == None or head.next == None:
        return head
    tail = head
    for i in range(k): 
        if tail == None:
            return head
        tail = tail.next
    newhead = reverse(head, tail)
    head.next = self.reverseKGroup(tail, k)
    return newhead