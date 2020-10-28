'''
제곱근을 찾는 문제
이분탐색으로 구할 수 있다.
아마 math.sqrt도 이렇게 구현되어있지 않을까?
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        while l <= r:
            mid = l+r>>1
            if mid*mid == x: return mid
            elif mid*mid < x: l = mid+1
            else: r = mid-1
        return l-1