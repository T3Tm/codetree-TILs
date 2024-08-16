import sys
input = sys.stdin.readline

n, q = map(int, input().split())

li = [0] + [*map(int, input().split())]
left = [0]
value = li[1]
for i in range(1, n):
    value = max(value, li[i])
    left.append(value)

right = []#2,2 (3 ~ n)
value = li[-1]#1, 2, 3
for i in range(n,1,-1):#
    value = max(value, li[i])
    right.append(value)
right.append(0)
right.append(0)
right = right[::-1]
right.append(0)

for _ in range(q):
    a,b = map(int,input().split())
    print(max(left[a-1], right[b+1]))