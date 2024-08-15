li = [*map(int, input().split())]

result = [0]*10
for i in range(1,len(li)):
    if li[i] == 0:
        break
    
    result[li[i]//10 % 10] += 1
result[li[0]//10 % 10] += 1
for i in range(1, 10):
    print(f'{i} - {result[i]}')