x1,y1,x2,y2 = map(lambda x: int(x) + 1000, input().split())

x3,y3,x4,y4 = map(lambda x: int(x) + 1000, input().split())

board = [[0]*2002 for _ in range(2002)]

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        board[i][j] = 1

for i in range(x3,x4 +1):
    for j in range(y3, y4+1):
        board[i][j] = 0

minix = 2003
miniy = 2003
maxix = -1
maxiy = -1


for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        if board[i][j]:
            minix = min(minix, i)
            maxix = max(maxix, i)

            miniy = min(miniy, j)
            maxiy = max(maxiy, j)

print( (maxix - minix)*(maxiy - miniy))