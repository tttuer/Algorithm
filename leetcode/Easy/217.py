'''
중복된 수가 있는지 여부를 묻는 문제
set을 이용하면 찾을 수 있다.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s: return True
            s.add(num)
        return False