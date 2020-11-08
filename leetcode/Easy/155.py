'''
최소값을 O(1)에 찾는 stack을 구현하는 문제
넣을때마다 sorted_stk에 넣어줘서 풀었는데 다른 방법이 있지 않을까?
최소 인덱스를 가지는 배열을 하나 더 선언해서 현재의 최솟값을 계속 가리키게 하면 된다.(더 좋은 방법)
'''

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.sorted_stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.sorted_stk = sorted(self.stk)

    def pop(self) -> None:
        top = self.stk[-1]
        self.stk.pop()
        self.sorted_stk = sorted(self.stk)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.sorted_stk[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_index = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.min_index:
            self.min_index.append(0)
        else:
            if self.stk[self.min_index[-1]] > self.stk[-1]:
                self.min_index.append(len(self.stk)-1)
            else:
                self.min_index.append(self.min_index[-1])

    def pop(self) -> None:
        top = self.stk[-1]
        self.stk.pop()
        self.min_index.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk[self.min_index[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()