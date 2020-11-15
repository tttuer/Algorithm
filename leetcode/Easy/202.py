'''
1로 만들 수 있는 수인지 아닌지를 판별하는 문제
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            if n in s:
                return False
            if n == 1: break
            s.add(n)
            nn = 0
            while n > 0:
                nn += int(n%10)**2
                n //= 10
            n = nn
        return True