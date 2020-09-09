class ListNode:
    def __init__(self, x):
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

## 1. Iterative 迭代
## Time Complexity: O(n)
## Space Complexity: O(1)
def reverseList1(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur != None:
        next = cur.next 
        cur.next = pre
        cur = next
        pre = cur
    return pre

## 2. Recursive 递归
## Time Complexity: O(n)
## Space Complexity: O(n)
def reverseList2(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    rhead = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return rhead

## 3. 迭代
def reverseList3(head: ListNode) -> ListNode:
    if head == None:
        return
    pre = None
    cur = head
    p = cur.next
    while cur and p:
        cur.next = pre  ## 千万不要忘记了这一步，否则就变成了一个环
        t = p.next
        p.next = cur
        pre = cur
        cur = p
        p = t
    return cur

nums = [1,2,3,4,5]
head = create_list(nums)
res = reverseList3(head)
res

