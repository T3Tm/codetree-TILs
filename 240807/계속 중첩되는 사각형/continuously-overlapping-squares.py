n = int(input())
board = [[0] * 300 for _ in[0]*300]
plus = 0
for i in range(n):
    a,b,c,d = map(lambda x:x+100,map(int,input().split()))
    for i in range(a,c):
        for j in range(b,d):
            board[i][j] = plus
    plus = not plus
h = 0
for row in board:
    h += row.count(1)
print(h)