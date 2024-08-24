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
    connect_cnt[y] += connect_cnt[x]
    parent[x] = y

n, m = map(int, input().split())

parent = [-1] * (n+1)
connect_cnt = [1] * (n+1)

for _ in range(m):
    cmd,a,*b = input().split()
    if cmd == 'x':
        merge(int(a), int(b[0]))
    else:
        print(connect_cnt[int(a)])