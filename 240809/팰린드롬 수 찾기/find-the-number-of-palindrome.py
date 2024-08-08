n,m=map(int,input().split())
cnt = 0
for i in range(n,m+1):
    st = f'{i}'
    if st[:len(st)//2] == st[-(len(st)//2):][::-1]:
        cnt+=1
print(cnt)