n, k = map(int,input().split())

cnt = 0
dic = {}
for num in map(int,input().split()):
    cnt += dic.get(k - num, 0)
    dic[num] = dic.get(num, 0) + 1

print(cnt)