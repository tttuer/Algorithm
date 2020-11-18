'''
링크드 리스트를 거꾸로 만드는 문제
스택을 사용하여 해결하였다.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        stk = []
        while head != None:
            stk.append(head.val)
            head = head.next
        new_head = ListNode()
        cur = new_head
        while stk:
            cur.val = stk.pop()
            if stk:
                cur.next = ListNode()
                cur = cur.next
        return new_head