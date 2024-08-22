import sys
input = sys.stdin.readline

n, Q = map(int ,input().split())
word = f"#{'#'.join(input().strip())}#"

A = [0] * len(word)

r=q=-1

for i in range(len(word)):
    if r>=i:
        ii = 2 * q - i
        A[i] = min(r - i, A[ii])
    
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < len(word) and word[i + A[i] + 1] == word[i - A[i] - 1]:
        A[i] += 1
    
    if i + A[i] > r:
        r, q = i + A[i], i


for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x * 2 - 1, y * 2 - 1 #1 3
    idx = (x + y) >> 1
    if 2 * A[idx] + 1 >= y - x:
        print("Yes")
    else:
        print("No")