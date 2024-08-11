from bisect import bisect_left
n = int(input())
dp = []
end_line = []
#끝나는 시간 , value
for _ in range(n):
    s,e,p = map(int,input().split())
    idx = bisect_left(end_line,s)
    v = max(dp[:idx] + [0])
    if idx == len(dp):
        end_line.append(e)
        dp.append(v+p) 
    elif end_line[idx] == e:
        dp[idx] = max(dp[idx], v + p)
    else:
        end_line.insert(idx,e)
        dp.insert(idx,v + p)
print(max(dp))