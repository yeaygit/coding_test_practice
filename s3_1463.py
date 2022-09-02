import sys

n= int(sys.stdin.readline())

"""
1-> 1 (0)
2-> 1 (1)
3-> 1 (1)
4-> 3->1 (2)
5-> 4->2->1(3)
6-> 3->1 (2)
7-> 6->3->1 (3)
8-> 4->2->1 (3)
9-> 3->1 (2)
10-> 9->3->1 (3)
아! 이렇게 풀어봤을때 어떻게 해야지 시간제한 안뜰까 고민중이었는데
4->3이 될때 1을 빼면 3이되고 앞에 3의 갯수를 가지면 됨..!
10일 때도 ->5,->9 가 있는데 ->5로가면 1+3개 ->9로 가면 1+2=3개가 된다
"""

c_cal=[0,0,1,1]

for i in range(4,n+1):
    c_cal.append(c_cal[i-1]+1) #우선 (-1)된 값에 -한 연산을 +1한 값을 넣어두고
    #c_cal.append로만 사용가능함 왜냐면 배열을 길이 4까지만 정의해놨기 때문에
    
    if i%3==0:
        c_cal[i]=min(c_cal[(i//3)]+1,c_cal[i]) #-1한 값과 //3한 값을 비교해 작은 값을 넣기
        
    if i%2==0:
        c_cal[i]=min(c_cal[(i//2)]+1,c_cal[i])
     

print(c_cal[n])