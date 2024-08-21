n = int(input())

#0 - > 1
#2 -> 3
# 3 -> 4
# 4 -> 6
# 7 -> 8
# 8 -> 23

#0,1
#2,3
#3,4
#4,6
#7,8
#1,9
#8,23

li = [[*map(int,input().split())]for _ in range(n)]

li.sort(key = lambda x:(x[1], x[0]))

end = 0
cnt = 0
for s,e in li:
    if end <= s:
        cnt += 1
        end = e
print(n-cnt)