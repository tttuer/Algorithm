class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = '0'*(len(b)-len(a))+a
        elif len(b) < len(a):
            b = '0'*(len(a)-len(b))+b
        l = 0
        ans = ''
        for i in range(len(a)-1,-1,-1):
            s = int(a[i])+int(b[i])+l
            l = s//2
            ans = str(s%2)+ans
        ans = str(l)+ans if l == 1 else ans
        return ans