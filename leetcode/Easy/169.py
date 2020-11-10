'''
n/2개 있는 숫자 리턴하는 문제
dict를 이용하여 갯수를 센 후 n/2개 일때 리턴해주는 방법
정렬을 한 후에 n/2에 위치한 숫자 리턴
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        for num in dic.keys():
            if dic[num] > len(nums)//2:
                return num

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]