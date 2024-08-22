import sys
sys.setrecursionlimit(100002)
input = sys.stdin.readline
INF = 100001
n, m = map(int,input().split())

#모든 간선에 대해 그 간선을 잇는 두 정점 중 적어도 하나에는 물건이 놓여 있어야 한다.
#예를 들어 1번과 2번 정점이 있으면 1번과 2번 중에는 한 곳에는 물건이 있어야 한다.
#그럼 내가 있을 때, 다음 정점에 있을 수도 있고, 없을 수도 있다.

#이미 있는 곳에서는 이미 있기 때문에 없는 경우가 있을 수가 없다.
def dfs(node, state, pre):
    global item, dp
    if item[node] and not state:return 100001
    if dp[node][state]!=INF:return dp[node][state]
    dp[node][state] = state
    for next in graph[node]:
        if next == pre:continue
        if state:#현재 있기 때문에 다른 곳 next들은 있든 없든 상관 없음.
            dp[node][state] += min(dfs(next, 1, node), dfs(next, 0, node))
        else:#내가 없으니까 너는 무조건 켜있어야 함.
            dp[node][state] += dfs(next, 1, node)
    return dp[node][state]
graph = {}
for i in range(1,n+1):
    graph[i] = []

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)


dp = [[INF, INF] for _ in range(n+1)]
item = [0] * (n+1)
for num in map(int, input().split()):
    item[num] = 1#여기는 무조건 있음

v = min(dfs(1, 1, 0) ,dfs(1, 0, 0))#현재 노드에 있을 때 먼저
print(v - m)