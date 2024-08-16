import sys
input = sys.stdin.readline

n, q = map(int,input().split())
2 , 1, 1, 3, 2, 1

dol = [[0] * 4 for _ in range(n+1)]
for i in range(1,n+1):
    dol[i] = dol[i-1][::]
    
    num = int(input())

    dol[i][num] += 1

for _ in range(q):
    a, b = map(int,input().split())

    t1,o1,o2,o3 = dol[b]
    t1,m1,m2,m3 = dol[a-1]
    print(o1-m1, o2-m2, o3-m3)