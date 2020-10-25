'''
투 포인터를 이용해 특정 숫자를 지우는 방법(새로 리스트 할당X)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i