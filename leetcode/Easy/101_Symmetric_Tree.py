'''
대칭 형태인지 알아내는 문제
if l == null and r == null
if l == null or r == null
로 하면 현재 recur에서 쓴 4줄이 커버된다.
생각을 잘 하면 코드를 줄일 수 있네...
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.recur(root.left,root.right)
        
    def recur(self,l,r):
        if not l and not r: return True
        if not l and r: return False
        if l and not r: return False
        if l.val != r.val: return False
        else:
            if not self.recur(l.left,r.right): return False
            if not self.recur(l.right,r.left): return False
            return True