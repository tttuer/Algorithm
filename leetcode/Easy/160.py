'''
두 리스트의 최초 교차점을 찾는 문제
계속 전진하면서 set에 담고 있으면 바로 return
투포인터를 이용해 찾는 방법
pa,pb가 None이면 headB,headA를 가리키게 한다 그러면 둘 다 같은 길이를 이동할 것이기 떄문에
만나는 지점이 같아지게 된다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA != None and headB != None:
            if headA in s:
                return headA
            s.add(headA)
            if headB in s:
                return headB
            s.add(headB)
            headA = headA.next
            headB = headB.next
        while headA != None:
            if headA in s:
                return headA
            headA = headA.next
        while headB != None:
            if headB in s:
                return headB
            headB = headB.next
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        pa = headA
        pb = headB
        
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
            
        return pa