import sys
input = sys.stdin.readline

SIZE = 100001
def find(x):
    if parent[x] < 0 :return x
    #부모 노드
    cur = x
    while parent[cur] >= 0:
        cur = parent[cur]
    
    while parent[x] >= 0:
        next = parent[x]
        parent[x] = cur
        x = next#부모 따라가기, 해당 곳에 cur로 좌압
    
    return cur

def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:return
    if y > x: x,y = y,x
    parent[y] += parent[x]#이 정점의 부모 차수
    node_cnt[y] += node_cnt[x]#부모의 갯수
    parent[x] = y
    
n = int(input())
parent = [-1] * (SIZE)
node_cnt = [1] * (SIZE)#각 정점의 갯수

for _ in range(n):
    a, b = map(int,input().split())
    merge(a,b)#머지 해버리기
    print(node_cnt[find(a)])