t = '#' + input()
#문자열 t의 접두사 중 이를 뒤집었을 때 문자열 T의 부분 문자열이 되는 
#최장 접두사의 길이를 구하여라

left,right = 1, len(t) - 1

#최장 접두사가 3이라면 2도 가능
while left <= right:
    mid = (left + right) >> 1
    pattern = '#' + t[1:mid + 1][::-1]

    f =[0] * (mid + 1)
    f[0] = -1
    for i in range(1, len(pattern)):
        j = f[i-1]
        while j>=0 and pattern[j+1] != pattern[i]:
            j = f[j]
        
        f[i] = j+1
    
    j = 0
    for i in range(1, len(t)):
        while j >= 0 and pattern[j+1] != t[i]:
            j = f[j]
        
        j += 1
        if j == mid:
            left = mid + 1
            break
    else:
        right = mid - 1
print(right)