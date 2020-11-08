'''
정렬된 배열 안에서 둘의 합이 target이 되는 인덱스를 찾는 문제
binary_search를 이용해서 찾을 수 있다.
투 포인터로도 해결할 수 있다.
dict에 넣어서도 해결할 수 있다.
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(target,l,r):
            if l > r: return None
            mid = l+r>>1
            if numbers[mid] == target: return mid
            elif numbers[mid] < target:
                return binary_search(target,mid+1,r)
            else:
                return binary_search(target,l,mid-1)
        
        for i in range(len(numbers)):
            r = binary_search(target-numbers[i],i+1,len(numbers)-1)
            if r != None:
                return [i+1,r+1]
                
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l < r:
            s = numbers[l]+numbers[r]
            if s == target: return [l+1,r+1]
            elif s < target: l += 1
            elif s > target: r -= 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(numbers)):
            now = target-numbers[i]
            if now in dic:
                return [dic[now]+1,i+1]
            dic[numbers[i]] = i