'''
파스칼의 삼각형을 배열로 만드는 문제
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[] for i in range(numRows)]
        if numRows == 0: return ret
        
        ret[0].append(1)
        for i in range(1,numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j-1]+ret[i-1][j])
        return ret