n = int(input())

li = [0] + [int(input()) for _ in range(n)]

prefix = [0]*(n+1)
result = 0

dic = {0:0}
for i in range(1,n+1):#n번
    prefix[i] = (prefix[i-1] + li[i])%7
    #prefix와 가장 가까운 7의 배수 찾기?
    #각각 prefix에서 7의 배수 들을 찾기
    result= max(result, i - dic.get(prefix[i],i))
    dic[prefix[i]] = min(dic.get(prefix[i],i),i)#인덱스 지정
print(result)