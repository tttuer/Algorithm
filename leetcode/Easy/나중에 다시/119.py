'''
rowIndex번째 파스칼의 삼각형을 구하는 방법
두번째 방법을 어떻게 떠올렸을까...? 대단하다.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:        
        ret = [1]
        for i in range(1,rowIndex+1):
            t = []
            for j in range(i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(ret[j-1]+ret[j])
            ret = t
        return ret

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:        
        ret = [1]
        
        for _ in range(rowIndex):
            ret = [x+y for x,y in zip([0]+ret,ret+[0])]
        return ret