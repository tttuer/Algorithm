'''
모든 문자열을 살펴보며 하는 방법
첫번째는 for문을 이용하여 찾은 방법
두번째는 반으로 쪼개면서 찾는 방법
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        strs.sort()
        base = strs[0]
        ans = ''
        for i in range(1,len(base)+1):
            flag = True
            for j in range(1,len(strs)):
                if strs[j][:i] != base[:i]:
                    flag = False
                    break
            if flag:
                ans = base[:i]
        return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        else:
            s1 = self.longestCommonPrefix(strs[:len(strs)//2])
            s2 = self.longestCommonPrefix(strs[len(strs)//2:])
            min_len = len(s1) if len(s2) > len(s1) else len(s2)
            for i in range(1,min_len+1):
                if s1[:i] != s2[:i]:
                    return s1[:i-1]
            return s1[:min_len]
                