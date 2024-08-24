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

n, m = map(int, input().split())

parent = [-1] * (n+1)

cnt = 0#사이클 끊기
for _ in range(m):
    a, b = map(int ,input().split())
    a = find(a)
    b = find(b)

    if a == b:
        cnt += 1
    merge(a, b)

for i in range(1, n+1):
    if find(i) == i:#부모인 것 세기
        cnt += 1
print(cnt - 1)