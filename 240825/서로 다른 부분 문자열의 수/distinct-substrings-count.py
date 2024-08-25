word = input()

s = len(word)

save = set()

p = [31, 37]
m = [10**9 + 7, 10 ** 9 + 9]

p_pow = [[1]*s for _ in range(2)]

for k in range(2):
    for i in range(1, s):
        p_pow[k][i] = (p_pow[k][i-1] * p[k])%m[k]


def to_int(ch):
    return ord(ch) - ord('a') + 1

for cnt in range(1,s+1):#몇 개씩 자를 것인지
    my_hash = [0, 0]
    for i in range(cnt):
        for k in range(2):
            my_hash[k] = (my_hash[k] + p_pow[k][cnt - i - 1] * to_int(word[i]))%m[k]
    
    save.add(tuple(my_hash))

    for i in range(1, s - cnt + 1):
        for k in range(2):
            my_hash[k] = ((my_hash[k] - to_int(word[i-1]) * p_pow[k][cnt - 1])*p[k] + to_int(word[i + cnt - 1]) + m[k]) % m[k]
        save.add(tuple(my_hash))

print(len(save))