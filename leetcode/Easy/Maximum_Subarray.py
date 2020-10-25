'''
연속된 부분합 중 최대값을 찾는 문제
divide and conquer로 푸는 방법이 있는데 나중에 다시 도전해야겠다.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        data = [0]*len(nums)
        data[0] = s
        for i in range(1,len(nums)):
            if s < 0:
                s = nums[i]
            else:
                s += nums[i]
            data[i] = s
        return max(data)