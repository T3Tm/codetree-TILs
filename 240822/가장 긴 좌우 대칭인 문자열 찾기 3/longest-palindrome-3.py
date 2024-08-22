n, m = input().split()
word = f'#{"#".join(input())}#'

n = len(word)

A = [0] * n

r=q=-1
#r은 최대로 나온 idx
#q는 중앙 index
#abacaba
for i in range(n):
    if r >= i:#이전에 계산한 값이 있음
        ii = 2 * q - i
        A[i] = min(r - i, A[ii])#둘 중 더 작은 값으로 초기화
    
    if word[i] == m:
        A[i] = 0
        continue
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and word[i-A[i]-1] == word[i+A[i]+1] \
        and word[i-A[i]-1] != m:
        A[i]+=1#양쪽으로 같음
    
    if i + A[i] > r:#최고로 오른쪽 인덱스보다 더 나가게 됐음
        r, q = i + A[i], i

result = 0
for i in range(n):
    result = max(result, A[i]*2 + 1)

print(result // 2)