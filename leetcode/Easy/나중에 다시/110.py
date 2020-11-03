'''
균형잡힌 높이를 가진 트리인지를 판별하는 문제
첫번째 풀이는 왼쪽과 오른쪽 가보면서 각각의 최고 높이를 구하고 차이를 구하는 방법 대략 O(n^2)?
두번째 풀이는 왼쪽과 오른쪽으로 나뉘었을때 왼쪽과 오른쪽의 높이 차이를 구하는 방법 O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        if abs(self.get_max(root.left,1)-self.get_max(root.right,1)) > 1:
            return False
        if not self.isBalanced(root.left): return False
        if not self.isBalanced(root.right): return False
        return True
                
    def get_max(self,now,h):
        if not now: return 0
        max_h = h
        
        if now.left:
            max_h = max(max_h,self.get_max(now.left,h+1))
        if now.right:
            max_h = max(max_h,self.get_max(now.right,h+1))
        return max_h

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != float('inf')
        
    def depth(self,root):
        if not root: return 0
        
        l = self.depth(root.left)
        r = self.depth(root.right)
        if abs(l-r) > 1:
            return float('inf')
        
        return max(l,r)+1