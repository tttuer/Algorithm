'''
루트에서 리프노드까지 가는 최소 거리를 찾는 문제
리프노드에 도달했을때 최소 거리를 갱신하면서 진행한다.
큐로 풀면 리프노드에 도달한 시점의 거리를 리턴하면 될 것이다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 10**9
    
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.depth(root,1)
        return self.ans
        
    def depth(self,root,h):
        if self.ans <= h: return
        if not root.left and not root.right: 
            self.ans = min(self.ans,h)
        
        if root.left:
            self.depth(root.left,h+1)
        if root.right:
            self.depth(root.right,h+1)