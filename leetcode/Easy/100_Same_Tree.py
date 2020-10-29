'''
트리가 같은지 비교하는 문제
재귀로 좌,우를 똑같이 돌면서 비교하면 된다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q: return False
        if p and not q: return False
        if not p and not q: return True
        if p.val != q.val: return False
        else:
            if not self.isSameTree(p.left,q.left): return False
            if not self.isSameTree(p.right,q.right): return False
            return True