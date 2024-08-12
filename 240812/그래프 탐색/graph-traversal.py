n,m=map(int,input().split())
graph = {}
for i in range(1,n+1):graph[i] = []

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[0]*(n+1)

s = [1]
visited[1] = 1
while s:
    cur = s.pop()
    for next in graph[cur]:
        if visited[next]:continue
        visited[next] = 1
        s.append(next)
print(visited.count(1) - 1)