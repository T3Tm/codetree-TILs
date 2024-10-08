'''
N명이 존재하며, M개의 치즈가 있음

M개 중 1개가 상했음

D번의 log가 있고 p, m, t

S번의 아픔 log가 있음 (이외의 사람이 아플 수도 있음)
p, t

data[초][누가] = d번
data[번][누가] = 초

N M D S

x x x x
1이 1번 먹음 1초
1이 4번 먹음 1초
1이 2번 먹음 2초
3이 1번 먹음 3초
1이 3번 먹음 4초
2이 1번 먹음 5초
2이 2번 먹음 7초

1번 3초에 아픔 2초에 먹은 것
2이 8초에 아픔

1번 2번
'''
minute_to_eat = {}#초에 누가 몇 번의 치즈를 먹었는지
cheese_to_eat = {}#몇 번 치즈를 누가 몇 초에 먹었는지


n,M,d,s = map(int,input().split())
for _ in range(d):
    p,m,t = map(int,input().split())
    minute_to_eat[t] = minute_to_eat.get(t,{})
    minute_to_eat[t][p] = m

    cheese_to_eat[m] = cheese_to_eat.get(m,{})
    cheese_to_eat[m][p] = min(cheese_to_eat[m].get(p,101),t)

sick = set()

sick_minute = {}
for _ in range(s):
    p,t = map(int,input().split())
    sick_minute[p] = t

#m개의 치즈
for i in range(1,M+1):
    i_cheese = cheese_to_eat.get(i,{})
    #i_cheese를 먹은 사람들 알아내기
    sick_set = set(sick_minute.keys()) & set(i_cheese.keys())
    if len(sick_set) == len(sick_minute.keys()):#아픈 사람 집합
        #그럼 이 아픈 사람들이 아프기 직전에 이 치즈를 먹었는지 확인
        flag = True
        for who in sick_set:
            time = sick_minute[who]#아픈 시간
            if cheese_to_eat[i][who] >= time:#i번 치즈를 who가 먹은 시간
                flag = False
                break
        if not flag:#이 조합은 아님
            continue
        #이러면 이 치즈를 먹은 사람들은 다 아플 거임
        for who in i_cheese.keys():
            sick.add(who)
print(len(sick))