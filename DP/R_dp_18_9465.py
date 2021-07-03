'''
분류 : 다이나믹 프로그래밍
문제 : 스티커 (백준 9465)
작성일자 : 2021.07.04
'''

# 목적 : 스티커 최대 점수 출력
# 접근 : dp 
#       1. 최적 부분 구조 (두칸 전까지의 최대값을 갱신하며 다음 문제 해결)
#       2. 부분 중복 문제 (이전에 계산한 값을 지속적으로 사용()
#       점화식 ai = 현재위치 + 두칸 전까지의 최댓값, 바로 직전 대각선의 값(계속 갱신) 중 큰 값

import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(2)]

    if N == 1 : 
        print(max(map(max, lst)))
    elif N >= 2 : 
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]
        if N == 2 : 
            print(max(map(max, lst)))
        else : 
            max_val = max(lst[1][0], lst[0][0])
            for i in range(2, N) : 
                lst[0][i] = lst[0][i] + max(lst[1][i-1],max_val)
                lst[1][i] = lst[1][i] + max(lst[0][i-1],max_val)
                max_val = max(lst[1][i-1],lst[0][i-1])
            print(max(map(max, lst)))