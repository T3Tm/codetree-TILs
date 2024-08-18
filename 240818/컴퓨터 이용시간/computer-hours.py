import sys
from heapq import*
input = sys.stdin.readline

n = int(input())

li = [[*map(int,input().split())] + [i] for i in range(n)]

li.sort(key = lambda x: x[0])

computer = []

result = [0]*n
for (s, e, idx) in li:
    num = len(computer) + 1
    while computer and computer[0][0] < s:#
        pree, preidx = heappop(computer)
        num = min(num, preidx)
    result[idx] = num#
    heappush(computer, (e, num))
print(*result)