import sys
sys.setrecursionlimit(100002)
input = sys.stdin.readline
LOG = 19

n = int(input())

graph = {}
for i in range(1, n+1):
    graph[i] = []


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

k = int(input())

def dfs(cur, prev):
    global height
    table[cur][0] = prev
    height[cur] = height[prev] + 1
    for next in graph[cur]:
        if next == prev:continue
        dfs(next, cur)

table = [[0]*LOG for _ in range(n+1)] 
color = [[0]*LOG for _ in range(n+1)]
height = [0] * (n+1)#각 높이 계산

for _ in range(k):
    num = int(input())
    color[num][0] = 1

dfs(1, 0)#그래프 작성하면서 table 채워봅시다.
for i in range(1, LOG):#i승
    for node in range(1, n+1):#현재 
        table[node][i] = table[table[node][i-1]][i-1]
        color[node][i] = color[table[node][i-1]][i-1]


query = int(input())

for _ in range(query):
    a, b = map(int, input().split())
    
    if height[a] > height[b]:a,b = b,a#스왑

    cnt = 0
    for i in range(LOG-1, -1, -1):
        if height[b] - height[a] >= 1 << i:#높이 맞춰주기
            cnt += color[b][i]
            b = table[b][i]
    
    #높이 맞춰줬으니
    if a == b:#만약 둘이 같다면 그냥 현재 갯수 덧셈
        print(cnt + color[b][0])#그리고 갯수 출력
    else:#둘이 다르므로 올라가면서 갯수 세주기
        for i in range(LOG-1, -1, -1):
            if table[a][i] != table[b][i]:#둘의 부모가 다르기 직전까지만 올라가면 된다.
                cnt += color[b][i]
                b = table[b][i]

                cnt += color[a][i]
                a = table[a][i]
        #부모가 이제 같음 그러면 
        print(cnt + color[b][0] + color[a][0] + color[table[b][0]][0])