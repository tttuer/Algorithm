'''
괄호 쌍이 맞는지 판별하는 문제
check에 쌍에 대한 정보를 넣어놓고 비교한다.
check = {')':'('} 이런식으로 비교해도 된다. 
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        check = {')':1,'(':2,'}':3,'{':4,']':5,'[':6}
        for c in s:
            if c == ')' or c == '}' or c == ']':
                if not stk or check[c]+1 != check[stk[-1]]:
                    return False
                stk.pop()
            else: stk.append(c)
        if stk: return False
        return True