def bact(depth):
    global word, result, s,idx
    if depth == idx:
        ret = s[word[0]]
        for i in range(1,len(word),2):
            if word[i] == '+':
                ret += s[word[i+1]]
            elif word[i] == '-':
                ret -= s[word[i+1]]
            else:
                ret *= s[word[i+1]]
        result = max(result,ret)
        return
    for i in range(1,5):
        s[s[depth]] = i
        bact(depth + 1)
        s[s[depth]] = 0
word = input()
s = {}
idx = 0
for i in word:
    if i.isalpha():
        prev = len(s)
        s[i] = 0
        after = len(s)
        if prev != after:
            s[idx] = i
            idx += 1
result = -1 * (10 ** 10)
bact(0)
print(result)