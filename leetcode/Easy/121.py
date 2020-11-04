'''
최저에 사고 최고에 파는 방법을 구하는 문제
스택인줄 알았는데 큐인 문제...
쭉 가면서 최솟값 갱신하고 그때그때 최대값을 갱신하면 되는 문제이다.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stk = []
        max_ = 0
        for price in prices:
            if not stk:
                stk.append(price)
            else:
                if stk[0] > price:
                    while stk:
                        stk.pop()
                else:
                    max_ = max(max_,price-stk[0])
                stk.append(price)
        return max_


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_,max_ = float('inf'),0
        for price in prices:
            min_ = min(min_,price)
            profit = price-min_
            max_ = max(max_,profit)
        return max_