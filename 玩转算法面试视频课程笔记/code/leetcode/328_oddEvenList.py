def oddEvenList(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    ph1 = ListNode(0)
    ph2 = ListNode(0)
    pre1 = ph1
    pre2 = ph2
    cur = head
    i = 0
    while cur:
        i += 1
        next = cur.next
        if i % 2 == 1:
            pre1.next = cur
            cur.next = None
            pre1 = cur
        else:
            pre2.next = cur
            cur.next = None
            pre2 = cur
        cur = next
    pre1.next = ph2.next
    return ph1.next
