from collections import deque
import sys
input = sys.stdin.readline

n = int(input())


graph = [[]for _ in range(n+1)]

indegree = [0]*(n+1)
take_time = [0]*(n+1)
for i in range(1,n+1):#i를 짓기 전에
    li = [*map(int,input().split())]
    take_time[i] = li[0]
    for j in range(1,len(li)-1):
        graph[li[j]].append(i)#애를 짓기 전에 j를 먼저 지어야함?
        indegree[i] += 1


dp = [0]*(n+1)
q = deque()

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
        dp[i] = take_time[i]

while q:
    cur = q.popleft()
    for next in graph[cur]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[cur])
        if not indegree[next]:
            q.append(next)
            dp[next] += take_time[next]

for i in range(1,n+1):
    print(dp[i])