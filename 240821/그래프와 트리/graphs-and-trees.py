def find(x):
    if parent[x] < 0:return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y :return

    if x < y:#더 크다면
        x,y = y,x
    #x가 무조건 더 큰 것
    parent[y] += parent[x]
    parent[x] = y
n, m = map(int,input().split())
#정점이 n
parent = [-1]*(n+1)

graph = {}
for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

flag = False
def dfs(cur, prev):# 1 -> 2 -> 3 -> 4
    global flag
    visited[cur] = 1#방문 처리
    cur_parent = find(cur)#나의 집합
    for next in graph[cur]:
        if next == prev:continue#부모 이므로 다시 안 가기
        if not visited[next]:
            merge(cur_parent, find(next))#같은 집합으로 만들어주기
            dfs(next, cur)
        else:#방문 인데, 같은 집합이면 없애기
            next_parent = find(next)#해당 집합이 나와 같다면?
            if next_parent == cur_parent:
                #사이클 생김
                #해당 집합이 불가능하다는 것을 체크해놓기
                visited[cur_parent] = 2 #해당 부모에다가 사이클 생겼다는 체크
for i in range(1,n+1):
    if visited[i]:continue
    dfs(i, 0)

cnt = 0
for i in range(1,n+1):
    if parent[i] < 0:#일단 집합의 부모임
        if visited[i]!=2:cnt += 1
print(cnt)