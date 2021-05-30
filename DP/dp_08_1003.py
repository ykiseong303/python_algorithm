'''
분류 : 다이나믹 프로그래밍
문제 : 피보나치 함수 (백준 1003)
작성일자 : 2021.05.30
'''

# 목적 : N번째 피보나치 수를 만들 때, 0과 1이 각각 호출되는 횟수 출력
# 접근 : 0, 1, 2 ... 번째 피보나치 수를 만들 때 필요한 0,1의 수를 기록
#       각 N번째에 대해 0과 1의 호출횟수를 규칙에 따라 dp테이블을 만들어도 가능
#       아니면 바로 아래의 풀이처럼 정해진 규칙에 따라 N번째까지의 0, 1의 호출 수를 기록
#       조건 1 > 0번째 에서의 값이 1번째의 값에 영향(작>큰, 이전>다음)

T = int(input())
for _ in range(T) : 
    N = int(input())
    zero, one = 1,0
    for _ in range(N) : 
        temp = one
        one = zero + one
        zero = temp
    print(zero, one)

'''T = int(input())
for _ in range(T) : 
    zero_cnt, one_cnt = 0, 0
    N = int(input())
    if N == 0 : 
        print(1, 0)
    elif N == 1 : 
        print(0, 1)
    else : 
        d1 = [0] * (N+1)
        d2 = [0] * (N+1)
        d1[0], d1[1] = 1,0
        d2[0], d2[1] = 0,1
        for i in range(2,N+1) : 
            d1[i] = d1[i-1] + d1[i-2]
            d2[i] = d2[i-1] + d2[i-2]
        print(d1[N], d2[N])
'''
