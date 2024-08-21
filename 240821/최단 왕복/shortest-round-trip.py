import sys
input = sys.stdin.readline

INF = 0x3f3f3f3f

n, m = map(int, input().split())


dist = [[INF] * (n+1)for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = c



for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

result = INF
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :continue
        if dist[i][j] + dist[j][i] < result:
            result = dist[i][j] + dist[j][i]
print(result)