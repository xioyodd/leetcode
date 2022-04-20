# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA