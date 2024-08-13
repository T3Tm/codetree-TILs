n = int(input())

li = [*map(int,input().split())]
#a의 합과 b를 같게 하되, 합이 최대가 되도록 하여라.
#sum(a) == sum(b) 이렇게 해놓고
li.sort()
#나머지 숫자는 C에 들어갔다고 생각하면 되는 거 아닌가?
#정확히 sum(li)이 2개로 나뉜다면 
#한 곳으로 보내고 나머지에 b로 갔다고 생각하면 된다.
#최대한 안 빼고 만드는 것이 좋음
total = sum(li)

#if total%2 == 0:#정확히 2등분 가능할 수도 있음

dp = [[0]*(total+1)for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

result = 0
for num in li: # n
    for j in range(total, num -1,-1):#100,000
        if dp[0][j-num]:
            dp[0][j] = 1    
#합이 total / 2

for k in range(n):#k 인덱스 값을 지웠을 때 되는지 확인
    if (total - li[k]) % 2 != 0:continue
    for i in range(n):
        if i == k:continue
        for j in range(total, li[i]-1,-1):#100,000
            if dp[k+1][j-li[i]]:
                dp[k+1][j] = 1

for i in range(1,n+1):
    if dp[i][(total - li[i-1]) >> 1]:
        result = max(result,(total - li[i-1]) >> 1)
    
if total % 2 == 0 and dp[0][total >> 1]:
    result = max(result, total >> 1)
print(result)