n = int(input())
t = int(input())
cnt = 1
now = 1
for i in range(1,n):
    now_num = int(input())
    if now_num != t:
        now = 1
    else:
        now += 1
    t = now_num
    cnt = max(cnt, now)
print(cnt)