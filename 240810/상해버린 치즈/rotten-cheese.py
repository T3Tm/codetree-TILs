minute_to_eat = {}#초에 누가 몇 번의 치즈를 먹었는지
cheese_to_eat = {}#몇 번 치즈를 누가 몇 초에 먹었는지


n,M,d,s = map(int,input().split())
for _ in range(d):
    p,m,t = map(int,input().split())
    minute_to_eat[t] = minute_to_eat.get(t,{})
    minute_to_eat[t][p] = m

    cheese_to_eat[m] = cheese_to_eat.get(m,{})
    cheese_to_eat[m][p] = t

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
    if sick_set:#아픈 사람 집합
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