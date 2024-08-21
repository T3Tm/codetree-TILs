import sys
from heapq import*
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int,input().split())

graph = {}
for i in range(1,n+1):
    graph[i] = {}

for _ in range(m):
    i,j,d = map(int,input().split())
    graph[i][j] = d
    graph[j][i] = d

#elogv

#학교에서 다익 돌린다.

dist = [INF] * (n+1)
def d(cur, dist):
    dist[cur] = 0
    q = []
    heappush(q, (0, cur))
    while q:
        dis, cur = heappop(q)
        
        if dist[cur] < dis:continue
        for next, value in graph[cur].items():
            if dis + value < dist[next]:
                dist[next] = dis + value
                heappush(q, (dist[next], next))

d(n, dist)
print(max(dist[1:]))