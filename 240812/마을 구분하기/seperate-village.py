n = int(input())
board = [[*map(int,input().split())]for _ in range(n)]



visited= [[0]* n for _ in range(n)]
house = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or not board[i][j]:continue
        
        visited[i][j] = 1
        s = [(i,j)]
        cnt = 0
        while s:
            x,y = s.pop()
            cnt += 1
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                nx,ny = x + dx, y + dy
                if nx < 0 or nx >=n or ny < 0  or ny >=n:continue
                if not board[nx][ny] or visited[nx][ny]:continue
                visited[nx][ny] = 1
                s.append((nx,ny))
        house.append(cnt)
print(len(house))
print(*sorted(house),sep = '\n')