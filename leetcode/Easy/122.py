'''
여러번을 팔아서 최고의 수익을 얻는 방법을 구하는 문제
스택을 사용하여 제일 위에 있는 값이 현재 값보다 크면 스택 가장 아래와 위를 뺴서 더한다
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stk = []
        sum_ = 0
        for price in prices:
            if not stk: stk.append(price)
            else:
                if stk[-1] > price:
                    sum_ += stk[-1]-stk[0]
                    while stk: stk.pop()
                stk.append(price)
        if stk:
            sum_ += stk[-1]-stk[0]
        return sum_