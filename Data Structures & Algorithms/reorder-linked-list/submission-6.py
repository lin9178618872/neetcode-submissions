# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 找中点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半部分
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # 3. 像 mergeTwoLists 一样合并
        first = head
        second = prev

        dummy = ListNode(0)
        curr = dummy

        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = second
            second = second.next
            curr = curr.next

        # 4. 把剩余部分接上
        if first:
            curr.next = first
        if second:
            curr.next = second

        # 5. 把结果放回 head
        head.val = dummy.next.val
        head.next = dummy.next.next
        