'''
아마 문제는 KMP 알고리즘을 원한거 같지만 index로 해결할 수 있다.
하지만 needle이 haystack안에 존재하지 않을 수 있기에 먼저 in으로 있는지 여부를 확인한다.

아래는 KMP알고리즘을 활용하여 구현한 부분이다.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

class Solution:
    def failure(self,key):
        if not key: return []
        pi = [0]
        j = 0
        for i in range(1,len(key)):
            while j > 0 and key[i] != key[j]: j = pi[j-1]
            if key[i] == key[j]:
                j += 1
                pi.append(j)
                if j == len(key):
                    j = pi[j-1]
            else:
                pi.append(j)
        return pi
    
    def kmp(self,string,key):
        if not key: return 0
        pi = self.failure(key)
        j = 0
        for i in range(len(string)):
            while j > 0 and string[i] != key[j]: j = pi[j-1]
            if string[i] == key[j]:
                j += 1
                if j == len(key):
                    return i-len(key)+1
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        return self.kmp(haystack,needle)