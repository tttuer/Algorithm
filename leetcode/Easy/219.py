'''
같은 수의 index차이가 k이하 인것이 있는지 여부를 묻는 문제
dict을 활용하면 풀 수 있다.
at most = 많아야, 기껏해야
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _dict = {}
        for i,num in enumerate(nums):
            if num in _dict:
                if i-_dict[num] <= k: return True
                elif i-_dict[num] > k: _dict[num] = i
            else:
                _dict[num] = i
        return False