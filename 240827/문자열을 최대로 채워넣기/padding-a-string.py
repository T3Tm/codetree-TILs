t, m = input().split()
t = '#'+ t
m = int(m)


pattern = [*map(lambda x: '#'+x, input().split())]
f=[[0]*10001 for _ in range(m)]

for k in range(m):
    f[k][0] = -1

    for i in range(1, len(pattern[k])):
        j = f[k][i-1]
        while j >= 0 and pattern[k][j+1] != pattern[k][i]:
            j = f[k][j]
        
        f[k][i] = j + 1
#모든 곳에 실패함수 만들고

dp = [0]*len(t)
j_m = [0] * m
for i in range(1, len(t)):

    for k in range(m):
        while j_m[k] >= 0 and pattern[k][j_m[k] + 1] != t[i]:
            j_m[k] = f[k][j_m[k]]
        j_m[k] += 1

        if j_m[k] == len(pattern[k])-1:
            j_m[k] = f[k][j_m[k]]

            dp[i] = max(dp[i], dp[i - (len(pattern[k])-1)] + len(pattern[k])-1)
    dp[i] = max(dp[i], dp[i-1])
print(dp[-1])