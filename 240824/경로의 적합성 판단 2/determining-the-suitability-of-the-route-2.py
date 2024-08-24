import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y :return

    if y > x:x,y = y,x

    parent[y] += parent[x]
    parent[x] = y

n,m,k = map(int ,input().split())
parent = [-1] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    merge(a,b)

li = [*map(int, input().split())]
for i in range(1,len(li)):
    pr = find(li[i-1])
    ne = find(li[i])
    if pr != ne:
        print(0)
        exit(0)
print(1)