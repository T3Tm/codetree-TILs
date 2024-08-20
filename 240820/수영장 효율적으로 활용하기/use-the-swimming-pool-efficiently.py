n, m = map(int, input().split())

li = [*map(int,input().split())] 


left, right = 1, sum(li)

while left<=right:
    mid = (left +right) >> 1#각 레인당 즐길 수 있는 값
    cnt = 1
    now = 0
    for i in range(n):#15, 11, 16, 15
        if li[i] > mid:#애초에 불가능
            cnt = m + 1
            break
        if now + li[i]<=mid:
            now += li[i]
        else:#넘어감!
            cnt += 1
            now = li[i]
    if cnt > m:#레인을 더 넘어가게 써야 됨 그러면 mid를 늘려서 한 레인당 쓸 수 있는 시간을 늘리자
        left = mid + 1
    else:
        right = mid - 1
print(left)