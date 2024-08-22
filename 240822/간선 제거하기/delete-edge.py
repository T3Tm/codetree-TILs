import sys
sys.setrecursionlimit(100002)
input = sys.stdin.readline


#간선의 가중치를 최대한 많이 지우고 싶다.
# 모든 정점이 연결돼있으면서
# 뺄 수 있는 간선의 가중치 최대?
#즉 연결돼있는 것들이 n-1개를 연결해서 가중치가 최소가 된다면
#나머지 m - (n-1)개 들이 최대로 뺄 수 있는 것이다.
def find(x):
    if parent[x] < 0:return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(x,y):
    x = find(x)
    y = find(y)

    if x==y:return
    if y > x:x,y=y,x
    parent[y] += parent[x]
    parent[x] = y
n, m = map(int,input().split())
parent = [-1] * (n+1)
graph = [[*map(int,input().split())]for _ in range(m)]

graph.sort(key = lambda x: x[2])

total = 0
for a,b,c in graph:
    total += c

def kruskal(g):
    global n
    ret = 0
    cnt = 0
    for a,b,c in g:
        if cnt == n-1:break
        a = find(a)
        b = find(b)
        if a!=b:
            cnt += 1
            merge(a,b)
            ret += c
    return ret

print(total - kruskal(graph))