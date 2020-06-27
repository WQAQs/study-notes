
def deleteDuplicatesII(self, head: ListNode) -> ListNode:
    if head == None:
        return None
    ph = ListNode(0)
    ph.next = head
    pre = ph
    cur = pre.next
    while cur:
        n = 0
        p = cur.next
        while p != None and p.val == cur.val:
            p = p.next
            n += 1
        if n > 0:
            cur = p
            pre.next = cur
        else:
            pre = cur
            cur = cur.next
    return ph.next
