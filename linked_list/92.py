# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 这个成员变量总觉得怪怪的
    nth_next = None
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.nth_next = head.next
            return head
        nth = self.reverseN(head.next,n-1)
        head.next.next = head
        head.next = self.nth_next
        return nth
        
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head,right)
        # 注意right也要减一
        head.next = self.reverseBetween(head.next,left-1,right-1) 
        return head