n,t = map(int,input().split())
cmd = input()
board = [[*map(int,input().split())]for _ in range(n)]

startx=starty=n//2
direc = 0

mov = (-1,0),(0,1),(1,0),(0,-1)
s = board[startx][starty]

for c in cmd:
    if c == 'R':
        direc = (direc + 1)%4
    elif c == 'L':
        direc = (direc - 1  + 4) % 4
    else:
        dx,dy = mov[direc]
        nx,ny = startx + dx, starty + dy
        if nx < 0 or nx >= n or ny < 0 or ny>=n:continue
        s += board[nx][ny]
        startx,starty = nx,ny
print(s)