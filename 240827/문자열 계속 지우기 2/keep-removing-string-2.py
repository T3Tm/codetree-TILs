#문자열 A와
#문자열 B가 주어진다.


A = '#' + input()
B = '#' + input()


f = [0]*len(B)
f[0] = -1 
for i in range(1, len(B)):
    j = f[i-1]
    while j>=0 and B[j+1] != B[i]:
        j = f[j]

    f[i] = j + 1


j = 0
result = []
for i in range(1, len(A)):
    while j>=0 and B[j+1] != A[i]:
        j = f[j]
    
    j += 1
    result.append([A[i], j])
    if j == len(B) - 1:#패턴 찾음
        cnt = len(B) - 1
        while cnt:
            result.pop()
            cnt -=1
        if result:
            j = result[-1][1]
        else:
            j = 0
print(''.join(map(lambda x:x[0], result)))