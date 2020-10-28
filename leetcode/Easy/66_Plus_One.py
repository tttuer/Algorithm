'''
리스트의 수를 이어붙여서 1을 더한 후 다시 리스트로 만드는 문제
map과 join을 이용하면 쉽게 풀 수 있다.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int,str(int("".join(map(str,digits)))+1)))