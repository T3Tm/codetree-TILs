#1 <= 수 <=m

m = int(input())
a, b = map(int,input().split())

mini = m
maxi = 0
for num in range(a,b+1):
    cnt = 0
    left,right = 1, m
    while left<=right:
        mid = (left+right) >> 1
        cnt+=1
        if mid == num:break
        if mid > num:
            right = mid - 1
        else:
            left = mid + 1
    maxi = max(maxi, cnt)
    mini = min(mini, cnt)
print(mini, maxi)