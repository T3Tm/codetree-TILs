#2011 m1월 d1이 월요일
#2011 m2월 d2은 어떤 요일
#2011의 2월은 28일까지

month = [0, 31, 28, 31,30,31,30,31,31,30,31,30,31]

m1,d1,m2,d2 = map(int,input().split())
#현재 월요일
day = 1#일, 월, 화, 수, 목, 금, 토
out = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

if m1 < m2:
    while m1 != m2:
        if d1 > month[m1]:#
            d1 -= month[m1]
            m1 += 1
            continue
        d1 += 7#7일씩 돌리기
else:
    while m1!=m2:
        if d1 < 0:#
            m1 -= 1
            d1 += month[m1]
            continue
        d1 -= 7#7일씩 돌리기
#일 수 맞추기 d2 < d1이러면 대참사
if d1 < d2:#내가 증가되면 됨.
    #일주일 안에 있어야 한다.
    while max(d1,d2) - min(d1,d2) > 7:#7안으로 들어오면 끝
        d1 += 7
else:
    while max(d1,d2) - min(d1,d2) > 7:#7안으로 들어오면 끝
        d2 += 7

gap = d2 - d1#
day = (day + gap)%7
print(out[day])