n = int(input())
li = [0] * 300002
color = [[0,0]for _ in range(300002)] 
idx = 200000
for i in range(n):
    a,b = input().split()
    plus = 1 if b == 'R'else -1
    for i in range(int(a)):
        if not (color[idx][0] == 2 and color[idx][1] == 2):
            li[idx] = 1 if b == 'R' else 2
            color[idx][b == 'R'] += 1
        if color[idx][0] == 2 and color[idx][1] == 2:
            li[idx] = 3
        if i == int(a)-1:break
        idx += plus
print(li.count(3), li.count(1), li.count(2))