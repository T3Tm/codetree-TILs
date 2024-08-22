from heapq import*
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#키가 큰 사람부터 내림차순으로 서있다.

#5,4,3,2,1
#n명의 친구는 모두 키가 다르며, 어떤 순서로 서있는지 대한 단서가 주어짐

#(a, b)형태
#a가 b번 친구보다 키가 크다.

#a > b 그러면 a는 b보다는 앞에 서야 겠네

graph = [[]for _ in range(n+1)]

indegree = [0]*(n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


q = []

for i in range(1,n+1):
    if not indegree[i]:
        heappush(q, i)

result = []
while q:
    cur = heappop(q)
    result.append(cur)
    for next in graph[cur]:
        indegree[next] -= 1
        if not indegree[next]:
            heappush(q, next)

if len(result) == n:
    print(*result)
else:
    print(-1)