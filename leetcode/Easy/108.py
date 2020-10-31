'''
정렬된 배열을 이진트리로 만드는 방법
이진트리의 높이는 왼쪽과 오른쪽이 같아야 한다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.recur(nums,0,len(nums))
        
    def recur(self,nums,s,e):
        if s >= e: return None
        else:
            mid = s+e>>1
            left = self.recur(nums,s,mid)
            right = self.recur(nums,mid+1,e)
            return TreeNode(nums[mid],left,right)