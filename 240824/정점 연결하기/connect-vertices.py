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

n = int(input())

parent = [-1] * (n+1)

for _ in range(n-2):
    a, b = map(int, input().split())
    merge(a,b)

cnt = []
for i in range(1, n+1):
    if find(i) == i:#부모임
        cnt.append(i)

print(*cnt)