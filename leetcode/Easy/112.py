'''
루트노드에서 리프노드까지 합 중 만족하는 합이 있는지 여부를 구하는 문제
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        return self.get_sum(root,0,sum)
        
    def get_sum(self,root,sum_,goal):
        if not root.left and not root.right: 
            sum_ += root.val
            return sum_ == goal
        
        if root.left:
            if self.get_sum(root.left,sum_+root.val,goal):
                return True
        if root.right:
            if self.get_sum(root.right,sum_+root.val,goal):
                return True
        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        
        if sum-root.val == 0 and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)