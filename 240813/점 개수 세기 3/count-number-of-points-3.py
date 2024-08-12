from bisect import bisect_left,bisect_right
n, q = map(int,input().split())

li = [*map(int,input().split())]
li.sort()

for _ in range(q):
    a,b = map(int,input().split())
    left = bisect_left(li,a)
    right = bisect_right(li,b)
    print(right - left)