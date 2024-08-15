n, k = map(int, input().split())

dic = {}
for i in range(2, n):
    dic[i] = {}

li = [*map(int,input().split())]

cnt = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        dic[j+1][li[i] + li[j]] = dic[j+1].get(li[i] + li[j], 0) + 1


for z in range(2, n):
    cnt += dic[z].get(k - li[z], 0)
print(cnt)