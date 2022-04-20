# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        # 下面千万不能改变先后顺序
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
