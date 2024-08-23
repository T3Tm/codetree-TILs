x1,y1,x2,y2 = map(lambda x: int(x) + 100, input().split())

x3,y3,x4,y4 = map(lambda x: int(x) + 100, input().split())

board = [[0]*202 for _ in range(202)]

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        board[i][j] = 1

for i in range(x3,x4 ):
    for j in range(y3, y4):
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
if minix == 2003:print(0)
else:
    print((maxix - minix)*(maxiy - miniy))