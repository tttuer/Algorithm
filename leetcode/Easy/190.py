'''
n을 2진수로 바꾸어 뒤집은 뒤 그 수를 다시 10진수로 나타내는 문제. 32비트를 모두 채워야 한다.
string으로 바꾸어 해결하였다.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0: return 0
        s = bin(n)[2:]
        ns = ''
        s = s[::-1]
        l = 32-len(s)
        for _ in range(l):
            s += '0'
        flag = False
        for i in range(len(s)):
            if s[i] != '0':
                flag = True
            if not flag: continue
            ns += s[i]
        return int(ns,2)