'''
인접한 집을 훔치지 않고 가장 많은 돈을 훔치는 방법
dp를 이용하여 전집을 훔치는 경우와 훔치지 않는 경우를 비교한다
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0]*(len(nums)+1)
        if not nums: return 0
        cache[1] = nums[0]
        for i in range(2,len(cache)):
            cache[i] = max(cache[i-1],cache[i-2]+nums[i-1])
        return cache[-1]