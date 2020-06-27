def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    vals, cur = [], head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
