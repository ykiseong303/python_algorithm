'''
분류 : 다이나믹 프로그래밍
문제 : 쉬운 계단 수 (백준 10844)
작성일자 : 2021.06.03
'''

# 목적 : 길이가 N인 계단 수가 총 몇 개 있는지 출력 
# 접근 : 끝자리가 0~9가 되는 계단 수를 구한다
#       끝자리가 1인 경우는 두자리 수는 21 이고 세자리 수는 21로 시작할 떼 121 321 등 
#       끝자리가 2로 시작하는 경우와 1로 시작하는 경우의 합으로 나타낼 수 있음
#       이전 문제로 큰 문제를 해결할 수 있음

N = int(input())
d = [[0]* 10 for _ in range(N)] 
# dp테이블을 초기화 
for i in range(10) : 
    if i == 0 : 
        d[0][i] = 0
        continue
    d[0][i] = 1
for i in range(1,N) : 
    for j in range(10) : 
        if j == 0 : 
            d[i][j] = d[i-1][j+1]
            continue
        if j == 9 : 
            d[i][j] = d[i-1][j-1]
            continue
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]
sum = 0
for i in range(10) : 
    sum += d[N-1][i] 
print(sum%1000000000)