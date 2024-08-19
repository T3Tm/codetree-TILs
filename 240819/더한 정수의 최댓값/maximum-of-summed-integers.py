n = int(input())
li = [*map(int,input().split())]
if li[0]+li[1] < li[-1] + li[-2]:
    print(2*sum(li[2:]))
else:
    print(2*sum(li[:-2]))