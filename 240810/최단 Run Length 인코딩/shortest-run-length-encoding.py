from collections import deque
word = input()
q = deque([*word])
cnt = 10 ** 8
for i in range(len(word)):
    q.rotate(1)
    words = ''.join(q)
    now = 0
    idx = 0
    while idx < len(words):
        inner = idx
        while inner < len(words) and words[idx] == words[inner]:
            inner += 1
        now += 2
        idx = inner
    cnt = min(cnt,now)
print(cnt)