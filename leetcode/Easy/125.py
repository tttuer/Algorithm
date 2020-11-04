'''
문자열에서 숫자,알파벳로만 된 것이 팰린드롬 형식인지 판별하는 문제
python string에서 isalnum()은 숫자 혹은 알파벳인지를 판별해준다.
유용할 것 같으니 기억하고 있자!
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [i for i in s.lower() if 'a' <= i <= 'z' or '0' <= i <= '9']
        return t == t[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [i for i in s.lower() if i.isalnum()]
        return t == t[::-1]