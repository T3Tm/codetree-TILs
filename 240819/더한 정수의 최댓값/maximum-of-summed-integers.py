n =int(input())
li=[*map(int,input().split())]
v=sum(li[2:])*2
vv=sum(li[:-2])*2
index = li[1:].index(min(li[1:-1]))+1
vvv=sum(li[1:index+1])+sum(li[index:-1])
print(max(v,vv,vvv))