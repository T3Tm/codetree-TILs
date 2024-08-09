n = int(input())
li = [*map(int,input().split())]
#두 개씩 묶었을 때 최솟값이 최대가 돼야한다.
li.sort()
result = 10 ** 9
for i in range(n):
    result = min(result, li[i+n]-li[i])
print(result)