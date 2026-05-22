# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 初始化前一个节点为 None
        curr = head  # 当前节点是链表的头节点
        
        while curr:  # 遍历链表，直到到达末尾
            temp = curr.next  # 暂存当前节点的下一个节点
            curr.next = prev  # 将当前节点的 next 指向前一个节点，反转链表
            prev = curr  # 移动前一个节点指针。y成为x对应prev=curr
            curr = temp  # 移动当前节点指针.z成为y
        
        return prev  # 返回新的头节点（原链表的尾节点）
