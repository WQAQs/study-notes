def reverseBetween(self, head, m, n):
    if head == None or head.next == None:
        return head
    ph = ListNode(0)
    ph.next = head
    pre = ph 
    cur = head
    i = 0
    while cur:
        i += 1
        if i == m:
            headpre = pre
        if i == n:
            tail = cur.next
            break
        pre = cur
        cur = cur.next
    cur = headpre.next
    pre = tail
    while cur != tail:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    headpre.next = pre
    return ph.next
    
        

        
