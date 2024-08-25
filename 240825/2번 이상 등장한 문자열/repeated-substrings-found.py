word = input()
s = len(word)
# 2번 이상 등장한다.
# 이분탐색이네

# 최장길이가 3이었다면
# aba 


p = [31, 37]
m = [10**9 + 7, 10**9 + 9]
p_pow = [[1]*s for _ in range(2)]
for k in range(2):
    for i in range(1,s):
        p_pow[k][i] = (p_pow[k][i-1] * p[k])%m[k]

def to_int(ch):
    return ord(ch) - ord('a') + 1

left, right = 1, s
while left<=right:
    mid = (left+right) >> 1
    
    #mid 일 때 있는지 확인
    dic = {}
    my_hash = [0, 0]
    for k in range(2):
        for i in range(mid):
            my_hash[k] = (my_hash[k] + p_pow[k][mid - i - 1] * to_int(word[i]))%m[k]
    
    dic[tuple(my_hash)] = 1

    flag = 0
    for i in range(1, s - mid + 1):
        for k in range(2):
            my_hash[k] = ((my_hash[k] - (to_int(word[i-1]) * p_pow[k][mid - 1])) * p[k] + to_int(word[i + mid - 1]) + m[k])%m[k]
        dic[tuple(my_hash)] = dic.get(tuple(my_hash), 0) + 1
        
        if dic[tuple(my_hash)] >1:
            flag = 1
            break
    if flag:
        left = mid + 1
    else:
        right = mid - 1
print(right)