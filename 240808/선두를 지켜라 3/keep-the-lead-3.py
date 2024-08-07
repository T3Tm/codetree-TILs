def B(board,n):
    last=1
    for _ in range(n):
        v,t = map(int,input().split())
        for i in range(last,last+t):
            board[i] = board[i-1] + v
        last += t
n,m=map(int,input().split())
n_board = [0]*(10**6+3)
m_board = n_board[::]

B(n_board,n)
B(m_board,m)
lastV = -1
cnt = 0
for i in range(1,10**6+3):
    if n_board[i] == m_board[i] == 0:break
    t = 0
    if n_board[i] > m_board[i]:t = 1
    elif n_board[i] < m_board[i]:t = 2
    else:t = 3

    if t!= lastV:cnt+=1
    lastV = t
print(cnt)