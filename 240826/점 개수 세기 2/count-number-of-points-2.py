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
        if y <= ny:
            search[x].append(ny)

for x in x_pos:#2500
    search[x].sort()

for _ in range(q):
    x1, y1, x2, y2 = map(int ,input().split())
    left_point = bisect_left(x_pos, x1)#이 지점부터
    left_x_point = x_pos[left_point]

    right_point = bisect_left(x_pos, x2)#이 지점부터
    right_x_point = x_pos[right_point]
    
    #list 
    left_y_point = bisect_left(search[left_x_point], y1)

    bigger_y1_cnt = len(search[left_x_point]) - left_y_point
    #1,2,3,4,5
    right_y_point = bisect_right(search[right_x_point], y2)
    bigger_y2_cnt = len(search[right_x_point]) - right_y_point

    print(bigger_y1_cnt - bigger_y2_cnt)