word = f'#{"#".join(input())}#'


n = len(word)

A = [0]*n

r=q=-1

for i in range(n):
    if r >= i:
        ii = 2 * q - i
        A[i] = min(r-i, A[ii])

    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and word[i - A[i] - 1] == word[i + A[i] + 1]:
        A[i] += 1
    
    if i + A[i] > r:
        r, q = i + A[i], i

ans = 0
for i in range(n):
    if word[i]!='#':
        ans += 1
    ans += A[i]//2 
print(ans)