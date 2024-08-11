n = int(input())
def bact(depth,column, li):
    global n,result,board
    if depth == n:
        result = max(result,min(li))
        return
    for i in range(n):
        if column[i]:continue
        column[i] = 1
        li[depth] = board[depth][i]
        bact(depth + 1, column,li)
        column[i] = 0
        li[depth] = 0
    
board = [[*map(int,input().split())]for _ in range(n)]
column = [0] * n
result = 0
bact(0,column,[0]*n)
print(result)