n = int(input())
li = [*input().split()]
cnt = 0
for i in range(n):
    for j in range(i):
        if li[j] > li[i]:
            cnt += 1
print(cnt)