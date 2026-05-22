# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 创建一个假头节点
        dummy = ListNode(0)
        dummy.next = head#加到head的前面

        # 慢指针
        slow = dummy

        # 快指针
        fast = dummy

        # =====================
        # 先让 fast 走 n + 1 步
        # =====================

        step = 0
        while step < n + 1:
            fast = fast.next
            step += 1

        # =====================
        # fast 和 slow 一起走
        # =====================

        while fast:
            fast = fast.next
            slow = slow.next

        # =====================
        # 删除 slow 后面的节点
        # =====================

        slow.next = slow.next.next

        # 返回新头
        return dummy.next
