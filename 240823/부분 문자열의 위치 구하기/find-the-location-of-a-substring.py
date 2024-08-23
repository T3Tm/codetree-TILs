word = input()
target = input()

p = [31, 37]#
m = [10**9 + 7, 10**9 + 9]

p_pow = [[]for _ in range(2)]
for k in range(2):
    p_pow[k].append(1)
    for i in range(1,len(target)):
        p_pow[k].append((p_pow[k][-1] * p[k])%m[k])


def to_int(ch):
    return ord(ch) - ord('a') + 1


word_hash = [0,0]
target_hash = [0,0]
for k in range(2):
    for i in range(len(target)):
        word_hash[k] = (p_pow[k][len(target) - i - 1] * to_int(word[i]) + word_hash[k])%m[k]
        target_hash[k] = (p_pow[k][len(target) - i - 1] * to_int(target[i]) + target_hash[k])%m[k]


result = 500001

if word_hash == target_hash:
    result = 0

for i in range(1,len(word) - len(target)+1):
    for k in range(2):
        word_hash[k] = ((word_hash[k] - to_int(word[i-1]) * p_pow[k][-1]) * p[k] + to_int(word[i + len(target) - 1]) + m[k])%m[k]
    
    if word_hash == target_hash:
        result = min(result, i)
        break
print([result,-1][result == 500001])