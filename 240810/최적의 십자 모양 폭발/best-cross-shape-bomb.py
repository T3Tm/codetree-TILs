n = int(input()) 

board = [[*map(int,input().split())]for _ in range(n)]

def bomb(arr,x,y):
    for i in range(arr[x][y]):
        arr[min(x + i, n-1)][y] = 0
        arr[max(x - i, 0)][y] = 0
        arr[x][min(y + i, n-1)] = 0
        arr[x][max(y - i, 0)] = 0

def gravity(arr):
    cache = [[0]*n for _ in range(n)]

    
    for j in range(n):
        idx = -1
        for i in range(n-1,-1,-1):
            if arr[i][j]:
                cache[idx][j] = arr[i][j]
                idx -= 1
    
    for i in range(n):
        arr[i] = cache[i][::]
def find_Pair(arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                if j + 1 < n and arr[i][j] == arr[i][j+1]:
                    cnt += 1
                if i + 1 < n and arr[i][j] == arr[i+1][j]:
                    cnt += 1
    return cnt

result = 0
for i in range(n):
    for j in range(n):
        #i,j가 터진다고 생각
        cache = [row[::] for row in board]
        #bomb
        bomb(board,i,j)
        #gravity
        gravity(board)
        #쌍 찾기
        value = find_Pair(board)
        #원복
        board = [row[::] for row in cache]

        result = max(result,value)
print(result)