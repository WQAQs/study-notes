def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head == None:
        return None
    pre = head
    cur = pre.next
    while cur:
        p = cur
        while p != None and p.val == pre.val:
            p = p.next
        pre.next = p
        pre = p
        if pre != None:
            cur = pre.next
        else :
            break
    return head