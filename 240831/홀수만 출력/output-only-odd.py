a,b = map(int, input().split())


for i in range(a + (a%2 == 0), b+1,2):
    print(i, end=' ')