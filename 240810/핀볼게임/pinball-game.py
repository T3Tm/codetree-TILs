n = int(input())

board = [[*map(int,input().split())]for _ in range(n)]
def turn(x,y, dir):
    if not board[x][y]:return dir
    
    if board[x][y]==1:
        if dir == 0:return 1
        elif dir == 1:return 0
        elif dir == 2:return 3
        return 2
    else:
        if dir == 0:return 3
        elif dir == 1:return 2
        elif dir == 2:return 1
        return 0
def move(x,y, dir):
    move = (-1,0),(0,1),(1,0),(-1,0)
    nx, ny = x+ move[dir][0] , y + move[dir][1]
    return nx,ny
def ball(x, y, dir):
    ret = 1 #처음에 올라간 곳
    while 0 <= x < n and 0<= y < n:
        #올라간 곳이 방향 전환인지 확인
        dir = turn(x,y,dir)
        x,y = move(x,y,dir)
        ret += 1 
    return ret


#첫번째 행
#마지막 행
result = 0
for i in range(n):
    result = max(result,ball(0,i,2))
    result = max(result,ball(0,n - i - 1,0))

#첫번째 열
#마지막 열
for i in range(n):
    result = max(result,ball(i,0,1))
    result = max(result,ball(n - i - 1,0,3))

print(result)