# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        """
        1. [a,b]这与labuladong的代码不同
        2. a.father.next = a 依然成立，所以不是真正的反转了[a,b]，因为这个函数追溯不到单链表的a节点之前的节点
        """
        # showListNode(a)
        # print(a.val)
        # print(b.val)
        # 这一步遗忘了，很关键
        b_nxt = b.next
        pre = b.next
        cur = a
        while cur != b_nxt:
            # AttributeError: 'NoneType' object has no attribute 'next'
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        # return b
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        dummy = ListNode(next=head)
        cnt = 0
        a = dummy.next
        a_pre = dummy
        b = dummy
        # showListNode(dummy, 'dummy')
        while b.next != None:
            cnt += 1
            b = b.next
            if cnt % k == 0:
                # print('#'*5)
                # showListNode(dummy, 'dummy')
                # showListNode(a, 'start from a')
                # print('b:{}'.format(b.val))
                a_pre.next = self.reverse(a,b)
                # showListNode(dummy, 'dummy')
                # showListNode(b, 'start from b')
                # print('#'*5)
                a_pre = a
                b = a
                a = a.next
        return dummy.next


def showListNode(head: ListNode, msg: str):
    tmp = []
    while head != None:
        tmp.append(head.val)
        head = head.next
    print('{}: {}'.format(msg,tmp))

if __name__ == "__main__":
    head = ListNode(5,None)
    head = ListNode(4,head)
    head = ListNode(3,head)
    head = ListNode(2,head)
    head = ListNode(1,head)
    showListNode(head, 'whole list')
    sol = Solution()
    head = sol.reverseKGroup(head,2)
    showListNode(head, 'whole list')