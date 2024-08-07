n,b = map(int,input().split())
li = []
for i in range(n):
    a, B = map(int,input().split())
    li.append([a,B,a//2])
li.sort(key=lambda x:(x[0]+x[1],x[1] + x[2]))
cnt = 0
for i in range(n):
    b -= li[i][0]+li[i][1]
    if b < 0:
        b += li[i][0]+li[i][1]
        b -= li[i][1]+li[i][2]
        if b < 0:break
    cnt+=1
print(cnt)