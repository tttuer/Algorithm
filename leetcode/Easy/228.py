'''
이어져있는 숫자의 범위를 구하는 문제
다음 수를 보면서 +1이 같은 지를 보면 된다.
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        s = 0
        e = 0
        ret = []
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                e += 1
            else:
                if s != e:
                    ret.append(str(nums[s])+'->'+str(nums[e]))
                else:
                    ret.append(str(nums[s]))
                s = e = i+1
        if s != e:
            ret.append(str(nums[s])+'->'+str(nums[e]))
        else:
            ret.append(str(nums[s]))
        return ret