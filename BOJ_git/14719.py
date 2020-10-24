from collections import deque

'''
빗물이 고이는 지점은 가둬져 있는 지점이다.
이를 구하기 위해서 왼쪽과 오른쪽에 가둬진 지점이 어디인지를 찾는 과정을
스택을 이용해서 풀었다.
'''

H,W = map(int,input().split())
data = list(map(int,input().split()))
check = [False]*W

stk = deque()
ans = 0
for i in range(W):
    if not stk:
        stk.append((data[i],i))
    else:
        if stk[0][0] <= data[i]:
            while stk:
                t = stk.pop()
                if not check[t[1]] and stk:
                    ans += stk[0][0]-t[0]
                    check[t[1]] = True
        stk.append((data[i],i))

stk = deque()
for i in range(W-1,-1,-1):
    if not stk:
        stk.append((data[i],i))
    else:
        if stk[0][0] <= data[i]:
            while stk:
                t = stk.pop()
                if not check[t[1]] and stk:
                    ans += stk[0][0]-t[0]
                    check[t[1]] = True
        stk.append((data[i],i))

print(ans)