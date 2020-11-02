import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(V+1)
count = 0
cut = set()

def dfs(x,p,visited,cut):
    global count
    count += 1
    visited[x] = count
    ret = visited[x]
    for n in graph[x]:
        if n == p: continue
        if not visited[n]:

            low = dfs(n,x,visited,cut)
            if low > visited[x]:
                cut.add((x,n) if x < n else (n,x))
            ret = min(ret,low)
        else:
            ret = min(ret,visited[n])

    return ret

for i in range(1,V+1):
    if not visited[i]:
        dfs(i,0,visited,cut)

print(len(cut))
cut_l = sorted(list(cut))
for c in cut_l:
    print(c[0],c[1])