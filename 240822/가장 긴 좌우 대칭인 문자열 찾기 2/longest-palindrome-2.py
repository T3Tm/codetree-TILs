'''
문자열이 하나 주어졌을 때
해당 문자열의 부분 문자열 중 가장 긴 팰린드롬의 길이를 구해보자.

A[i] = i번지를 중심으로 홀수 길이의 팰린드롬 중 가장 긴 팰린드롬의 반지름의 길이

즉 [i - Ai, i + Ai]가 i를 중심으로 하는 최장 홀수 길이의 팰린드롬이 된다.

A[i-1]#이 j이라는 것은
현재 내 인덱스가 i일 때
A[i] = 아니네

e d c b a n a b c d e
'''

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
    
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and word[i-A[i]-1] == word[i+A[i]+1]:
        A[i]+=1#양쪽으로 같음
    
    if i + A[i] > r:#최고로 오른쪽 인덱스보다 더 나가게 됐음
        r, q = i + A[i], i

result = 0
for i in range(n):
    result = max(result, A[i]*2 + 1)

print(result // 2)