def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ph = ListNode(0)
    pre = ph
    cur1 = l1
    cur2 = l2
    carry = 0
    while cur1 or cur2 or carry:
        a = 0 if cur1 == None else cur1.val
        b = 0 if cur2 == None else cur2.val
        val = (a + b + carry) % 10
        node = ListNode(val)
        pre.next = node
        pre = node
        carry = 0 if a + b + carry < 10 else 1
        cur1 = cur1 if cur1 == None else cur1.next
        cur2 = cur2 if cur2 == None else cur2.next
    return ph.next


