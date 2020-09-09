class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def creat_list(nums):
    ph = ListNode(0)
    pre = ph
    for x in nums:
        cur = ListNode(x)
        pre.next = cur
        pre = cur
    return ph.next

def partition(head: ListNode, x: int) -> ListNode:
    if head == None or head.next == None:
        return head
    ph1 = ListNode(0)
    ph2 = ListNode(0)
    pre1 = ph1
    pre2 = ph2
    cur = head
    while cur:
        next = cur.next
        cur.next = None  ## 千万不要忘记！！否则最终返回的链表中会形成环
        if cur.val < x:
            pre1.next = cur
            pre1 = cur
        else:
            pre2.next = cur
            pre2 = cur
        cur = next
    pre1.next = ph2.next
    return ph1.next

nums = [1,2,3,4,5,2,2]
head = creat_list(nums)
res = partition(head,3)
res