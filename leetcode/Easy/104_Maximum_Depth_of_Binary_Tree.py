'''
이진 트리의 최대 깊이를 구하는 문제
재귀를 써서 해결할 수 있다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return self.get_max(root,1)
        
    def get_max(self,node,depth):
        if not node.left and not node.right: return depth
        else:
            ret = 1
            if node.left:
                ret = max(ret,self.get_max(node.left,depth+1))
            if node.right:
                ret = max(ret,self.get_max(node.right,depth+1))
            return ret