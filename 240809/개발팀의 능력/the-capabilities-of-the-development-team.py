from itertools import combinations
li = [*map(int,input().split())]

result = 10**8
#5C2
for combi in combinations(li,2):
    lis = []
    for i in range(5):
        if li[i] not in combi:
            lis.append(li[i])
    #3C2
    for comb in combinations(lis,2):

        if sum(combi) == sum(comb):continue

        last = -1
        for i in range(5):
            if li[i] not in combi and li[i] not in comb:
                last = li[i]
                break
        
        if sum(combi) == sum(comb) == last:continue
        
        l = sorted([sum(combi),sum(comb),last])
        result = min(result, l[-1] - l[0])
print([result,-1][result == 10 ** 8])