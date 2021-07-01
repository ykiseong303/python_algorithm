'''
분류 : 다이나믹 프로그래밍
문제 : 오르막 수 (백준 11057)
작성일자 : 2021.07.01
'''

# 목적 : 길이 N의 오르막 수의 총 개수를 출력
# 접근 : dp 
#       1. 이전 문제가 다음 문제에 영향 (N=2일때, 1로 시작한다면 1의 자리가 1~9까지 올 수 있는 경우)
#       2. 부분 중복문제 발생 (1~9까지의 연산이 지속적으로 발생)
#       초기 값에 대한 설정 필요

N = int(input())
d = [[1] * 10 for _ in range(N)]
for i in range(1,N) : 
    for j in range(10) : 
        if i == 1 and j == 0 : 
            d[i][j] = 10 
            continue
        d[i][j] = sum(d[i-1][j:])
res = 0
for i in range(10) : 
    res += d[N-1][i]
print(res%10007)
