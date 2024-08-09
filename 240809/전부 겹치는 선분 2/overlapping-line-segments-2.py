n = int(input())
board = [0] * 102
for i in range(n):
    x1,x2 = map(int,input().split())
    board[x1] += 1
    board[x2+1] -=1
result = 'No'
for i in range(1,102):
    board[i] += board[i-1]
    if board[i] >= n - 1:
        result = 'Yes'
        break
print(result)