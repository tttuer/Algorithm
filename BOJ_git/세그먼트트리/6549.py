import sys,math
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def init(tree,data,s,e,node):
    if s == e:
        tree[node] = s
        return tree[node]
    mid = s+e>>1
    m1 = init(tree,data,s,mid,node*2)
    m2 = init(tree,data,mid+1,e,node*2+1)
    if data[m1] <= data[m2]:
        tree[node] = tree[node*2]
    else:
        tree[node] = tree[node*2+1]
    return tree[node]

def query(tree,data,s,e,node,l,r):
    if e < l or r < s: return -1
    elif l <= s and e <= r: return tree[node]
    mid = s+e>>1
    m1 = query(tree,data,s,mid,node*2,l,r)
    m2 = query(tree,data,mid+1,e,node*2+1,l,r)
    if m1 == -1: return m2
    elif m2 == -1: return m1
    else:
        if data[m1] <= data[m2]:
            return m1
        else:
            return m2

def get_max(tree,data,s,e):
    m = query(tree,data,1,data[0],1,s,e)

    answer = (e-s+1)*data[m]

    if s <= m-1:
        answer = max(answer,get_max(tree,data,s,m-1))
    if m+1 <= e:
        answer = max(answer,get_max(tree,data,m+1,e))
    return answer

while 1:
    data = list(map(int,input().split()))
    if len(data) == 1:
        break
    h = 2**int(math.ceil(math.log2(data[0])+1))
    tree = [0]*h
    init(tree,data,1,data[0],1)
    answer = get_max(tree,data,1,data[0])
    print(answer)

# 참고: https://www.crocus.co.kr/707