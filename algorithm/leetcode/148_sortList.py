class Solution:
    ## 1. 归并排序
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        # 使用快慢指针寻找中心结点
        slow, fast = head, head.next  
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next




    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head or head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid , slow.next = slow.next, None
        left, right = sortList(head), sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val <= right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = right if right else left
        return res.next

