'''
비트로 따졌을때 1의 갯수를 세는 문제
1. 32비트이므로 32번 i를 시프트하여 갯수를 센다.
2. n이 0이 될때까지 n을 오른쪽으로 밀며 첫 비트가 1인지 검사하는 방법.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n & (1<<i): ans += 1
        return ans

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans