'''
액셀 차트에 맞는 이름으로 변환하는 문제
n-1을 해준 값으로 연산을 하면 되는 것을 몰랐다.
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        excel = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        ans = ''
        while n > 0:
            ans += excel[(n-1)%26]
            n = (n-1)/26
        return ans[::-1]