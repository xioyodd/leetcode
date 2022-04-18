# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        tmp = self.findNthFromEnd(dummy,n+1)
        tmp.next = tmp.next.next
        return dummy.next #不能return head
    def findNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        last = head
        for i in range(n):
            last = last.next
        nth = head
        while last != None:
            last = last.next
            nth = nth.next
        return nth