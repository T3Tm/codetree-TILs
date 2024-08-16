import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, q = map(int,input().split())

li = [*map(int,input().split())]

li.sort()

for _ in range(q):
    a, b = map(int,input().split())

    print(bisect_right(li, b) - bisect_left(li, a))