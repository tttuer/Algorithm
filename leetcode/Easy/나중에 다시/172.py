'''
팩토리얼에서 뒤에 연속하는 0의 갯수를 세는 문제
1. 숫자를 만들어보고 그 뒤에 0을 세는 방법
2. 해당 숫자까지 5의 갯수만을 세어 확인하는 방법(5로 계속 나누면서 갯수를 더해주는 것은 25에는 5가 5개, 125에는 5가 3개가 있기 때문이다.)
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 1
        for i in range(1,n+1):
            result *= i
        result = str(result)
        ans = 0
        for i in range(len(result)-1,-1,-1):
            if result[i] != '0': break
            ans += 1
            
        return ans

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n//5+self.trailingZeroes(n//5)