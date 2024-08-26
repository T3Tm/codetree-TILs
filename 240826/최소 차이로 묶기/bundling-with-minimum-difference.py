n, m = map(int, input().split())

arrn = [*map(int,input().split())]
arrm = [*map(int,input().split())]

arrn.sort(reverse=1)
arrm.sort(reverse=1)

result = 0
for i in range(min(n,m)):
    result += abs(arrn[i] - arrm[i])

print(result)