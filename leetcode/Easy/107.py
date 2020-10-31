'''
이진 트리의 순서를 가장 밑에서부터 리스트에 담는 문제
최대 깊이를 알아내고 최대 깊이 - 현재 깊이에 현재 값을 담아주어 해결
dict을 쓰는 방법을 잘 몰라서 이렇게 풀었다.

두번째 풀이는 dict을 이용하는 방법
depth가 dict안에 있다면 append, 없으면 리스트를 넣어주는 방식 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        cur = root
        d = self.get_max(cur,0)
        ret = [[] for _ in range(d)]
        cur = root
        self.recur(cur,1,d,ret)
        return ret
    
    def get_max(self,root,depth):
        if root == None: return depth
        else:
            d_max = 0
            d_max = max(d_max,self.get_max(root.left,depth+1))
            d_max = max(d_max,self.get_max(root.right,depth+1))
            return d_max
        
    def recur(self,root,depth,d,l):
        if root == None: return
        else:
            l[d-depth].append(root.val)
            self.recur(root.left,depth+1,d,l)
            self.recur(root.right,depth+1,d,l)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        s = {}
        self.recur(root,0,s)
        return [s[i] for i in sorted(s.keys(),reverse = True)]
        
    def recur(self,root,depth,s):
        if root == None: return
        else:
            if depth in s:
                s[depth].append(root.val)
            else:
                s[depth] = [root.val]
            self.recur(root.left,depth+1,s)
            self.recur(root.right,depth+1,s)