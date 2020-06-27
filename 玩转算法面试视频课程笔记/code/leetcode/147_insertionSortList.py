class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def create_list(nums):
    ph = ListNode(0)
    pre = ph
    for x in nums:
        cur = ListNode(x)
        pre.next = cur
        pre = cur
    return ph.next

def insertionSortList(head: ListNode) -> ListNode:
    ph = ListNode(0)
    ph.next  = head
    pre = ph.next
    while pre and pre.next:
        val = pre.next.val  # 选取这个结点，想要把它插入到前面的有序子链中的合适位置上
        next = pre.next.next
        pi = ph
        while pi != pre:
            if pi.next.val > val:
                swapnode = pre.next
                pre.next = pre.next.next
                pj = pi.next
                pi.next = swapnode
                swapnode.next = pj
                break
            pi = pi.next
        if pi == pre:  ## 一定不要忘了这个判断！只有在pi==pre时才是将要插入的结点接在了前面有序子链的末尾(其实就是没有做处理正常退出上面的循环)
            pre = pre.next
    return ph.next

nums = [4,2,1,3]
head = create_list(nums)
res = insertionSortList(head)
res



