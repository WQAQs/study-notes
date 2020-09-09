
# 1. 连成环，选择新的头结点，尾结点，拆开环并返回新的头节点
def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or not head.next:return head
    cur, n = head, 1
    while cur.next:
        cur = cur.next
        n += 1
    cur.next, cur = head, head
    for i in range(n-k%n-1):  #!!一定要注意取模！！
        cur = cur.next
    tail, rh, tail.next = cur, cur.next, None
    return rh