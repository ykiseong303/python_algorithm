'''
분류 : 다이나믹 프로그래밍
문제 : 파도반 수열 (백준 9461)
작성일자 : 2021.07.07
'''

# 목적 : N번째 정삼각형의 변의 길이를 출력
# 접근 : dp 
#       점화식 ai = a[i-3] + a[i-2]

T = int(input())
for _ in range(T) : 
    N = int(input())
    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    for i in range(4,101) : 
        d[i] = d[i-3] + d[i-2]
    print(d[N])