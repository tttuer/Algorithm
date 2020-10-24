'''
dict을 사용하여 빠르게 푸는 방법이 있다는 걸 배웠다.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        
        for i,v in enumerate(nums):
            n = target-v
            if n not in s:
                s[v] = i
            else:
                return [s[n],i]
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]