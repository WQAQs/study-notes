def mergeTwoLists(self, l1, l2):
    dh = ListNode(0)
    pre = dh
    cur1 = l1
    cur2 = l2
    while cur1 or cur2:
        if not cur1:
            pre.next = cur2
            break
        if not cur2:
            pre.next = cur1
            break
        # if cur1.val <= cur2.val:
        #     cur = cur1
        #     cur1 = cur1.next
        # else:
        #     cur = cur2
        #     cur2 = cur2.next
        # pre.next = cur
        # pre = pre.next
        if cur1.val <= cur2.val:
           pre.next, cur1 = cur1, cur1.next
        else:
           pre.next, cur2 = cur2, cur2.next
        pre = pre.next
    return dh.next