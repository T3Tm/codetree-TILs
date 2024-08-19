n = int(input())

#순서를 바꿔도 된다 == 해당 이루는 알파벳이 같다
# == 

dic = {}

for idx in range(n):
    word = input()
    
    alpha = {}
    for i in word:
        alpha[i] = alpha.get(i, 0) + 1
    
    dic[idx] = alpha#알파벳 갯수 세기

result = 0
for idx in range(n):
    now = 1
    for j in range(n):
        if idx == j:continue

        flag = True
        for key in dic[idx]:
            if dic[idx].get(key, -1) != dic[j].get(key, -2):
                flag=False
                break
        if flag:
            now+=1
    result = max(result, now)
print(result)