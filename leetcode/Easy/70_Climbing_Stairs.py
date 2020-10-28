'''
다이나믹 문제
신기한 점은 파이썬에서 memo 선언을 dict으로 하는걸 좋아하는 것 같다.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[1] = memo[0] = 1
        for i in range(2,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = memo[0] = 1
        for i in range(2,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]