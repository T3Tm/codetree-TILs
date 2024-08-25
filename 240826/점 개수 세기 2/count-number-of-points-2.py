from bisect import bisect_left, bisect_right
import sys
n, q = map(int, input().split())

li = []

x_pos = set()
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))
    x_pos.add(x)
li.sort()
li.append((10**9+1, 10**9 + 1))
x_pos = sorted(x_pos)
x_pos.append(10**9 + 1)

#정렬을 하는데
#for문 돌리면서 자신보다 큰 j만 갖고 오면 된다.
search = {}
for idx in range(n+1):
    x, y = li[idx]
    if x not in search:
        search[x] = []
    
    for j in range(idx, n+1):
        nx, ny = li[j]
        search[x].append(ny)

for x in x_pos:#2500
    search[x].sort()

for _ in range(q):
    x1, y1, x2, y2 = map(int ,input().split())
    
    #x1,y1에서 left 갯수 세기
    x1_point = x_pos[bisect_left(x_pos, x1)]
    total_cnt = bisect_left(search[x1_point], y1)

    #x2+1, y1 left갯수 세기
    x2_plus_point = x_pos[bisect_right(x_pos, x2)]
    x2_cnt = bisect_left(search[x2_plus_point], y1)

    #x1에서 y2 right 갯수
    x1_y2_cnt = bisect_right(search[x1_point], y2)
    
    #x2하나 크고, y2
    x2_y2_cnt = bisect_right(search[x2_plus_point], y2)
    x2_plus_len = len(search[x2_plus_point])
    x1_len = len(search[x1_point])
    print((x1_len - total_cnt) - (x1_len - x1_y2_cnt) - (x2_plus_len - x2_cnt) + (x2_plus_len - x2_y2_cnt))