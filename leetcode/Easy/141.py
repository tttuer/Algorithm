'''
방향 그래프에서 사이클의 여부를 판단하는 문제
해시를 이용해서 이미 갔던 곳을 또 방문하면 사이클
slow와 fast를 가지고 fast는 두번씩 slow는 한번씩 돌면 된다.
자세한 설명은 leetcode에서...
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while True:
            if not head:
                return False
            elif head in s:
                return True
            s.add(head)
            head = head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        
        while True:
            if not fast or not fast.next:
                return False
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next