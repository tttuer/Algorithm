'''
1. 스트링으로 만들어서 뒤집은 값과 같은지 비교
2. 스트링을 쓰지 않는 방법으론 음수이면 False, 양수일땐 mod를 사용하여 뒤집어 값을 만들고 기존 x와 비교
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        tx,nx = x,0
        while tx > 0:
            nx = nx*10+tx%10
            tx //= 10
        return x == nx