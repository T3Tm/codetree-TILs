from sortedcontainers import SortedSet
import sys
from heapq import*
input = sys.stdin.readline

n = int(input())

li = [[*map(int,input().split())] + [i] for i in range(n)]

li.sort(key = lambda x:x[0])

computer = []
computer_num = SortedSet([i for i in range(1,n+1)])

result = [0]*n
for (s, e, idx) in li:
    while computer and computer[0][0] <= s:#
        pree, preidx = heappop(computer)
        computer_num.add(preidx)
    result[idx] = computer_num[0]#제일 작은 숫자
    heappush(computer, (e, computer_num[0]))
    computer_num.discard(computer_num[0])
print(*result)