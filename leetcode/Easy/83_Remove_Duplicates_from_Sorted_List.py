'''
중복 노드를 삭제하는 문제
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None
        now = head.val
        cur = head.next
        root = head
        while cur != None:
            if cur.val != now:
                now = cur.val
                root.next = cur
                root = root.next
            cur = cur.next
        root.next = cur
        return head