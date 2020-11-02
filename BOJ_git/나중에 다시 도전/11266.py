import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(V+1)
cut = set()
count = 0
def dfs(x,is_root,visited,cut):
    global count
    count += 1
    visited[x] = count
    ret = visited[x]

    cnt = 0
    for i in graph[x]:

        if not visited[i]:
            cnt += 1

            low = dfs(i,False,visited,cut)
            if not is_root and low >= visited[x]:
                cut.add(x)
            ret = min(ret,low)
        else:
            ret = min(ret,visited[i])
    
    if is_root and cnt >= 2:
        cut.add(x)
    
    return ret

count = 0
for i in range(1,V+1):
    if visited[i]: continue
    dfs(i,True,visited,cut)

print(len(cut))
cut_l = sorted(list(cut))
for i in cut_l:
    print(i,end=' ')
print()

