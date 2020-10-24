'''
문자열로 만들어 뒤집어 준 뒤 반환
다만 예외 처리로 범위를 넘어갈 시 0리턴
'''

class Solution:
    def reverse(self, x: int) -> int:
        flag = True if x < 0 else False
        if flag:
            s = str(-x)
        else:
            s = str(x)
        result = -int(s[::-1]) if flag else int(s[::-1])
        if result < -2**31 or result > 2**31-1:
            result = 0
        return result