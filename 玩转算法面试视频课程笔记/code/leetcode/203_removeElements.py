def removeElements(self, head, val): 
    dummyhead = ListNode(0)
    pre = dummyhead
    pre.next = head
    cur = head
    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = pre.next
        else:
            pre = cur 
            cur = cur.next
    return dummyhead.next