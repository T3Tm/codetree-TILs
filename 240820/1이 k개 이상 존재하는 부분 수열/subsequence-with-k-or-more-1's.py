n, k =map(int,input().split())
li = [*map(int,input().split())]

s = 0
left = 0
right = 0
result = 1000001
while right <= n:
    if s < k:
        if right == n:break
        s += li[right] == 1
        right += 1
    else:#s >= k 되는 순간
        result = min(result,(right-1) - (left - 1))
        s -= li[left] == 1
        left += 1
print([result, -1][result == 1000001])