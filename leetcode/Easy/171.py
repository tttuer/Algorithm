'''
excel col을 숫자로 바꾸는 방법
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        idx = 0
        for i in range(len(s)-1,-1,-1):
            ans += 26**idx*(ord(s[i])-ord('A')+1)
            idx+=1
        return ans