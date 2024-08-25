t, q = input().split()
n = len(t)

t = '#' + t
for _ in range(int(q)):
    pattern = '#' + input()
    l = len(pattern) - 1
    f = [0] * (l+1)
    f[0] = -1
    
    for i in range(1, l+1):
        j = f[i-1]#이전 값
        
        while j >=0 and pattern[j+1] != pattern[i]:
            j = f[j]
            #같지 않다면 j만큼씩 땡겨서 다시 비교해보기
        f[i] = j + 1

    cnt = j = 0
    for i in range(1, n+1):
        
        while j >= 0 and pattern[j+1] != t[i]:
            j = f[j]
        
        j += 1
        
        if j == l:
            cnt += 1
            j = f[j]
    print(cnt)