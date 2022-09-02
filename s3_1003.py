import sys

c_zero=[1,0,1]
c_one=[0,1,1]

#fibo(3)-> c_zero,c_one[3]=1,2
#fibo(4)-> c_zero,c_one[4]=2,3
#fibo(5)-> c_zero,c_one[5]=3,5
#fibo(6)-> c_zero,c_one[6]=5,8
#--> c_zero 와 c_one도 피보나치 수열임을 알 수 있음

for i in range(3,1000):
    c_zero.append(c_zero[i-1]+c_zero[i-2])
    c_one.append(c_one[i-1]+c_one[i-2])


t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    print(c_zero[n],c_one[n])


"""
220902

처음 시간을 생각하지못하고 피보나치 수열에서 직접 0과1의 갯수를 생각하는 함수를 구현했다
그치만 시간초과를 경험 후 직접 계산해 나열해보았다
계산해보니 0과1의 갯수도 피보나치 수열이었고 이를 통해 위의 함수를 구현하게 되었다.
(print에서 공백으로 인한 출력형식 실수도 있었다.)
"""
