'''
replace를 이용해 변형이 될 수 있는 것들을 미리 바꿔준다.
이후 dict을 통해 변형될 숫자를 적어주고 이를 이용해 바꾼다.
replace는 해당 스트링을 바꿔주지 않기 때문에 재할당을 해야한다.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('IV','A') # 4
        s = s.replace('IX','B') # 9
        s = s.replace('XL','E') # 40
        s = s.replace('XC','F') # 90
        s = s.replace('CD','G') # 400
        s = s.replace('CM','H') # 900
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
              'A':4,'B':9,'E':40,'F':90,'G':400,'H':900}
        ans = 0
        for c in s:
            ans += dic[c]
        return ans