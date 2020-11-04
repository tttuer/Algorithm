'''
한개만 있는 수를 찾는 방법
dict을 이용해서 찾는 방법
XOR를 사용해서 찾는 방법(신기하다)
XOR는 같은 비트이면 0, 다른 비트이면 1을 반환한다.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        for num in dic.keys():
            if dic[num] == 1: return num
        return 0

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num
        return ret