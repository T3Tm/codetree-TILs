n = int(input())

# A랑 B에 차이가 최소가 돼야 한다.

# 즉 절반에 가깝게 채우면 된다.

# A를 절반에 가깝게 채웠다면
# 나머지를 B에 채우면 최소가 될 수 있을 것이다.
li = [*map(int,input().split())]

total = sum(li)
max_gap = li[1] - li[0]
mid = total >> 1
#li에서 i부터 시작하여

# 1 1000
dp = [[-1 for _ in range(total + 1)] for _ in range(n)]

#모든 n의 값은 0이다.
for i in range(n):
    dp[i][0] = 0

# 1 1000
# li[i] 자체만으로 
# 1 1000 , 1001, 2002 , 3003, 4004
result = 10 ** 8
for i in range(n):#li[i]를 이용하여 range를 채운다.
    #li[i]를 추가해서 mid에 가장 가까운 숫자를 찾아낸다.
    for j in range(total,0,-1):
        #case1 자기 자신을 더해서 나오는 경우의 수
        if dp[i][j-li[i]]!=-1 or dp[i-1][j-li[i]]!=-1:
            dp[i][j] = 1

        
        #case2 자기 자신을 더하지 않고 나오는 경우의 수
        if dp[i-1][j]!= -1:
            dp[i][j] = 1
        
        if dp[i][j] != -1 and j >= mid:
            result = min(result,j - mid)
 #이 결과
print(abs(total - (mid + result)* 2))