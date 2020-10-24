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
                