import math

#두원의 위치 관계
"""
(외접+내접(내접을 생각못함))
|r1+r2|==d -> 1점
|r1+r2|<d -> 0점
|r1+r2|>d -> 2점

내접(이건 생각을 못함;;)
or |r1-r2|==d -> 1점
|r1-r2|?d -> 0점 --> 위의 경우 전부 제외했을 때
and |r1-r2|<d -> 2점

x1==x2 and y1==y2 (중심이 같을 때)
-> r이 서로 다르면 0점
   r이 같으면 -1 출력
"""
def two_loc(x1,y1,r1,x2,y2,r2):
    d=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)

    else:
        if (r1+r2)==d or abs(r2-r1)==d:
            print(1)
        elif (r1+r2)>d and abs(r1-r2)<d:
            print(2)
        else:
            print(0)
        


loc_n=int(input())
for i in range(loc_n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    two_loc(x1,y1,r1,x2,y2,r2)