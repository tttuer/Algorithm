class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        now = '1'
        while i < n:
            s = now[0]
            new_str = ''
            cnt = 1
            for k in range(1,len(now)):
                if now[k] != s:
                    new_str += str(cnt)+s
                    s = now[k]
                    cnt = 1
                else:
                    cnt += 1
            new_str += str(cnt)+s
            now = new_str
            i += 1
        return now