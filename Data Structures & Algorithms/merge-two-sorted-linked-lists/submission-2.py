# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1️⃣ 创建一个虚拟头节点 dummy，方便操作
        dummy = ListNode(0)  
        curr = dummy  # 用 current 指针来追踪新链表的末尾

        # 2️⃣ 遍历两个链表，直到其中一个为空
        while list1 and list2:#等价于while list1 is not None and list2 is not None:
            if list1.val < list2.val:  # 选较小的节点
                curr.next = list1  # 把 list1 连接到 current.next
                list1 = list1.next  # list1 向前移动
            else:
                curr.next = list2  # 把 list2 连接到 current.next
                list2 = list2.next  # list2 向前移动
            
            curr = curr.next  # current 也向前移动
        
        # 3️⃣ 处理剩余的节点（其中一个链表还有未连接的部分）
        if list1:
            curr.next = list1  # 直接连接 list1 剩余的部分
        else:
            curr.next = list2  # 直接连接 list2 剩余的部分

        # 4️⃣ 返回合并后的链表（跳过 dummy 头节点）
        return dummy.next
