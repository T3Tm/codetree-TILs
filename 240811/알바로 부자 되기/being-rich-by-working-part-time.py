from bisect import bisect_left
n = int(input())
dp = [0]
end_line = [0]
#끝나는 시간 , value
def binary_search(e):
    left,right = 0,len(dp) - 1
    ret = 0
    while left <= right:
        mid = (left+right) >> 1
        if end_line[mid] >= e:
            right = mid - 1
        else:#이때는 되는데 제일 큰 value
            left = mid + 1
            ret = max(ret, dp[mid])
    return ret
    
for _ in range(n):
    s,e,p = map(int,input().split())
    v = binary_search(s)
    #s , e = p
    #s보다 작은 아이들 중 v가 가장 큰 아이
    idx = bisect_left(end_line,e)
    if idx == len(dp):
        end_line.append(e)
        dp.append(v+p) 
    elif end_line[idx] == e:
        dp[idx] = max(dp[idx], v + p)
    else:
        end_line.insert(idx,e)
        dp.insert(idx,v + p)
print(max(dp))