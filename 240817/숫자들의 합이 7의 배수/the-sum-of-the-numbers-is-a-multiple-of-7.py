n = int(input())

li = [0] + [int(input()) for _ in range(n)]

prefix = [0]*(n+1)
result = 0

dic = {0:0}
for i in range(1,n+1):#n번
    prefix[i] = prefix[i-1] + li[i]
    #prefix와 가장 가까운 7의 배수 찾기?
    #각각 prefix에서 7의 배수 들을 찾기
    temp = prefix[i]
    mul = 1
    while temp - mul * 7 >= 0:#13번 돈다.
        now_seven = mul * 7 #temp에서 가장 가까운 7의 배수 이 값이 (temp - div*7) 이 값이 dic에 있으면 result
        if temp - now_seven in dic:
            result = max(result, i - dic[temp-now_seven])
        mul += 1
    dic[prefix[i]] = i#인덱스 지정
print(result)