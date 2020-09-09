
def swapPairs(self, head: ListNode) -> ListNode:
    ph = ListNode(0)
    ph.next = head
    p = ph
    while p.next != None and p.next.next != None:
        node1 = p.next
        node2 = node1.next
        p.next = node2
        node1.next = node2.next
        node2.next = node1
        p = node1
    return ph.next
        
        