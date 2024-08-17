from heapq import*
import sys
input = sys.stdin.readline

n = int(input())

li = [[*map(int,input().split())]for _ in range(n)]

li.sort()

hotel = []
result = 0
for (s, e) in li:
    while hotel and hotel[0][0] <=s:
        heappop(hotel)
    heappush(hotel,[e,s])
    result = max(result, len(hotel))

print(result)