'''
링크드 리스트를 사용해 보는 문제
머지 소트의 기본 개념을 이용하면 쉽게 풀 수 있다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        rl = ListNode()
        root = rl
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                root.next = ListNode(l1.val)
                l1 = l1.next
            else:
                root.next = ListNode(l2.val)
                l2 = l2.next
            root = root.next
        while l1 != None:
            root.next = ListNode(l1.val)
            l1 = l1.next
            root = root.next
        while l2 != None:
            root.next = ListNode(l2.val)
            l2 = l2.next
            root = root.next
        return rl.next
        