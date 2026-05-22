# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:  # 如果链表为空或只有一个节点，直接返回
            return
        
        # 1. 找到链表的中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. 反转链表的后半部分
        second = slow.next
        slow.next = None  # 切断前半部分与后半部分的连接

        
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # 3. 合并两个链表
        first, second = head, prev
        while second:
            tmp1=first.next 
            tmp2 = second.next  # 暂存下一个节点
            first.next = second  # 将第二部分的节点接到第一部分
            second.next = tmp1  # 将第一部分的节点接到第二部分
            first= tmp1 
            second= tmp2  # 移动指针
        