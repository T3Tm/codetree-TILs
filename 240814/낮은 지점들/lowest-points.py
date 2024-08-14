#동일한 x좌표를 갖는 점들에 대해서는 가장 작은 y를 갖는 점을 제외한 다른 점들은 제거
#

n = int(input())

dic = {}
for _ in range(n):
    x,y = map(int,input().split())
    dic[x] = min(dic.get(x,10**9+1),y)
print(sum(dic.values()))