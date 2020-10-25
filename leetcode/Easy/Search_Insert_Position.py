'''
바이너리 서치 문제
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l+r>>1
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] == target:
                return mid
            else:
                l = mid+1
        return l