from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int , input().split())


arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int ,input().split())
    arr[a][b] = 1


q = deque([[1,1]])
dirs = {
    'U' : 0,
    'D' : 2,
    'R' : 1,
    'L' : 3
}

dx = [-1,0,1,0]
dy = [0,1,0,-1]


time = 0
for _ in range(k):
    dir, cnt = input().split()
    cnt = int(cnt)

    for i in range(cnt):
        x, y = q[0]
        nx,ny = x + dx[dirs[dir]], y + dy[dirs[dir]]
        time += 1
        if nx < 1 or nx > n or ny < 1 or ny > n:#종료 돼야함
            print(time)
            exit(0)
        
        #몸 박 확인
        for i in range(len(q)-1):
            if [nx, ny] == q[i]:#몸 박
                print(time)
                exit(0)
        
        if arr[nx][ny]:#해당 곳에 먹이가 있음
            arr[nx][ny] = 0
        else:#꼬리 줄이기
            q.pop()
        q.appendleft([nx, ny])
        
print(time)