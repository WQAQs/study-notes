# 1.第一次遍历得到链表长度，第2次遍历删除结点

# 2.使用双指针（间隔固定的快慢指针）
# 只用遍历一遍链表
def removeNthFromEnd(self, head, n):
    if not head: return
    dh = ListNode(0)
    dh.next = head
    slow, fast = dh, head
    for i in range(n):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dh.next