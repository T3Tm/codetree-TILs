n,b = map(int,input().split())
li = []
for i in range(n):
    a, B = map(int,input().split())
    li.append([a,B,a//2,i])
li.sort(key=lambda x: x[0]+x[1])
ins = set()
lis = sorted(li,key=lambda x: x[1] + x[2])
cnt = 0
flag = 0
for i in range(n):
    b -= li[i][0]+li[i][1]
    if b < 0:
        if flag:break
        b += li[i][0]+li[i][1]
        for j in range(n):
            if lis[j][3] not in ins:
                ins.add(lis[j][3])
                b -= lis[j][1] + lis[j][2]
                break      
        flag = 1
        if b < 0:break
        cnt +=1
        continue
    cnt+=1
    ins.add(li[i][3])
print(cnt)