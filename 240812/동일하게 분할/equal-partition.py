n = int(input())
a = [*map(int,input().split())]
if sum(a)/2 == sum(a) // 2:
    print('Yes')
else:
    print('No')