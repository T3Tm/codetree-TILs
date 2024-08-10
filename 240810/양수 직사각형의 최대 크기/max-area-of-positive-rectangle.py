n,m = map(int,input().split())
board = [[0]* (m+1)] + [[0] + [*map(int,input().split())] for _ in range(n)]

prefix = [[0]* (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix[i][j] = prefix[i][j-1] + (board[i][j] < 1)
#m^2 * n
result = -1
for i in range(1,m+1):
    for j in range(i,m+1):
        cnt,mx = 0,-1
        for row in range(1,n+1):
            if prefix[row][j] - prefix[row][i-1] == 0:
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt = 0
        result = max(result, mx * (j - i + 1))
print(result)