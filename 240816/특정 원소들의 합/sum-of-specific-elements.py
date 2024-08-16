board = [[*map(int,input().split())]for _ in range(4)]

total = 0

for i in range(4):
    total += sum(board[i][:i+1])
print(total)