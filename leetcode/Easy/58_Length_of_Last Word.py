'''
split 한 후 맨 마지막에 있는 문자의 길이를 반환하는 문제
함정은 split했을때 리스트에 아무것도 없는 경우가 있다.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = s.split()
        return len(sl[-1]) if sl else 0