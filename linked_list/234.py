# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def reverse(head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        right = self.reverse(slow)
        left = head
        while right is not None:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True
