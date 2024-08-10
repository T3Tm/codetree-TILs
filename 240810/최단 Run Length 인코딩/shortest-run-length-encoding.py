from collections import deque
word = input()
q = deque([*word])
cnt = 10 ** 8
for i in range(len(word)):
    q.rotate(1)
    words = ''.join(q)
    idx = 0
    b = ''
    while idx < len(words):
        inner = idx
        while inner < len(words) and words[idx] == words[inner]:
            inner += 1
        b += f'{words[idx]}{inner-idx}'
        idx = inner
    cnt = min(cnt,len(b))
print(cnt)