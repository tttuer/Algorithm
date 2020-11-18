'''
n까지의 소수를 세는 문제
에라토스테네스의체를 이용하면 빠르게 풀 수 있다.
'''

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0: return 0
        prime = [True]*(n+1)
        prime[0] = prime[1] = False
        for i in range(2,int(math.sqrt(n)+1)):
            if not prime[i]: continue
            for j in range(i+i,n+1,i):
                prime[j] = False
        count = 0
        for i in range(n):
            if prime[i]: count += 1
        return count