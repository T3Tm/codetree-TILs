n = int(input())

board = [[0] * (n+1)] + [[0] + [*map(int,input().split())]for _ in range(n)]

prefix = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + board[i][j] - prefix[i-1][j-1]


result = 0

for i in range(1, n-1):#1
    for j in range(1, n-1):
        result = max(result, prefix[i+2][j+2] - prefix[i+2][j-1] - prefix[i-1][j+2] + prefix[i-1][j-1])


print(result)