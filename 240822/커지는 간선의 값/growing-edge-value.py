import sys
from heapq import*
input = sys.stdin.readline


n, m, k = map(int,input().split())
#크루스칼은 ElogE
#프림은 정점이 있으면 연결된 간선 중 최소를 뽑아서 더해주는 방식으로 들어감
#간선들 중에서 하나 뽑는 거 (n-1)logE
#이건 아무곳에서든 시작해도 됨
graph = {}
for i in range(1,n+1):
    graph[i] = {}

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c


cnt = 0
total = 0

sucess = [0]*(n+1)
q = []
for next, value in graph[1].items():
    heappush(q, (value, next))

while 1:
    value, cur = heappop(q)#이렇게 돼서 나온 것이 연결된 것!
    if sucess[cur]:continue
    total += value + k*cnt 
    cnt += 1
    sucess[cur] = 1
    if cnt == n-1:break
    for next, value in graph[cur].items():
        if sucess[next]:continue#이미 연결된 정점이라면 굳이 볼 필요 없음
        heappush(q, (value, next))
        
print(total)