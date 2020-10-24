'''
스택을 활용하는 문제
()를 기준으로 )를 만나기 전까지는 모두 스택에 넣어놓는다
)를 만나면 스택 안을 살펴보며 (를 만날 때 까지 10이상의 숫자는 10을 빼서 cnt에 더해주고 아닌 것들은 1을 더해준다
(10을 뺴서 더해주는 이유는 계산된 값과 구분하기 위함이다.)
마지막엔 스택에 들어있는 값들을 카운트 해주면 길이가 나온다.
'''

from collections import deque
string = input()

stk = deque()

for i in range(len(string)):
    if string[i] != ')':
        if string[i] == '(':
            stk.append(string[i])
        else:
            stk.append(int(string[i]))
    else:
        cnt = 0
        while stk:
            if stk[len(stk)-1] == '(':
                stk.pop()
                break
            now = stk.pop()
            if now >= 10: cnt += now-10
            else: cnt += 1
        if stk:
            r = stk.pop()
            stk.append(cnt*r+10)
    
ans = 0
while stk:
    cur = stk.pop()
    if cur >= 10:
        ans += cur-10
    else:
        ans += 1
print(ans)

# 참고
# https://jjangsungwon.tistory.com/56