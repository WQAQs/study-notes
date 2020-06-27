class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(nums):
    ph = ListNode(0)
    pre = ph
    for x in nums:
        node = ListNode(x)
        pre.next = node
        pre = node
    return ph.next


## 1. 使用堆栈
## Time Complexity: O(m + n + max(m, n))
## Space Complexity: O(m + n)
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    stack1 = []
    stack2 = []
    res = []
    cur = l1
    while cur:
        stack1.append(cur.val)
        cur = cur.next
    cur = l2
    while cur:
        stack2.append(cur.val)
        cur = cur.next
    ph = ListNode(0)
    pre = ph
    carry = 0
    while carry or stack1 or stack2:
        a = 0 if len(stack1) == 0 else stack1.pop()
        b = 0 if len(stack2) == 0 else stack2.pop()
        sum = a + b + carry
        carry = 0 if sum < 10 else 1
        res.append(sum % 10)
    while len(res) != 0:
        cur = ListNode(res.pop())
        pre.next = cur
        pre = cur
    return ph.next

## 1. 使用堆栈的简单写法
## 使用头插法，就不需要dummynode了，并且建立返回链表时也不需要stack了
## Time Complexity: O(m + n + max(m, n))
## Space Complexity: O(m + n)
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    stack1, stack2 = [l1], [l2]
    while stack1[-1].next:
        stack1.append(stack1[-1].next)
    while stack2[-1].next:
        stack2.append(stack2[-1].next)
    carry, pre = 0, None
    while stack1 or stack2 or carry:
        carry += (stack1.pop().val if stack1 else 0) + (stack2.pop().val if stack2 else 0)
        head = ListNode(carry % 10)
        head.next = pre ## 使用头插法
        pre = head
        carry //= 10
    return head

## 2.递归Recursion
def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    def get_len(head):
        if not head:
            return 0
        return 1 + get_len(head.next)
    def add(l1,l2,carry):
        if not l1:
            carry = 0
            return None
        next = add(l1.next, l2.next,carry)
        sum = l1.val + l2.val + carry
        node = ListNode(sum%10)
        node.next = next
        carry = sum // 10
        return node
    len1, len2 = get_len(l1), get_len(l2)
    len = max(len1,len2)
    head = l1 if len1 < len2 else l2
    for i in range(len - min(len1,len2)):
        node = ListNode(0)
        node.next = head
        head = node
    if len1 < len2:
        l1 = head
    else:
        l2 = head
    carry = 0
    res = add(l1,l2,carry)
    if carry:
        node = ListNode(carry)
        node.next = res
        res = node
    return res

nums1 = [7,2,4,3]
nums2 = [5,6,4]
l1 = create_list(nums1)
l2 = create_list(nums2)
res = addTwoNumbers2(l1,l2)
res