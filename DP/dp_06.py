'''
분류 : 다이나믹 프로그래밍
문제 : 광산 (이코테 예제4)
작성일자 : 2021.05.28
'''

# 목적 : 채굴할 수 있는 최대크기를 출력
# 접근 : BFS, DP 
#   조건 1 > 0열의 최적해로 1열의 최적해를 구할 수 있음... (작 > 큰)
#   조건 2 > 기록해두지 않으면, 전에 구했던 것을 또 구해야함? (잘모르겠음)
#   점화식 : ai = i번째 열의 값 + 직전까지의 (3가지 경우) 최적해를 더한 값

import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    # 열의 개수만큼 끊어서 DP테이블에 저장
    dp = [] 
    arr = []
    for i in range(len(lst)) : 
        arr.append(lst[i])
        if len(arr) == m : 
            dp.append(arr)
            arr = []
            
    # 1열부터 시작
    for j in range(1,m) : # 열을 기준 (1열부터 시작)
        for i in range(n) : # 각열의 행을 하나씩 확인
            if i == 0 : left_up = 0 # 범위를 벗어나는 경우
            else : left_up = dp[i-1][j-1] # 왼쪽위의 값으로 갱신
            if i == n-1 : left_down = 0
            else : left_down = dp[i+1][j-1]
            left =  dp[i][j-1]
            # 현재값(i행 j열)은 현재값 + 직전(3가지 방향)까지의 최적해를 더한 값으로 갱신
            dp[i][j] = dp[i][j] + max(left_down,left_up,left)
    
    # 마지막 열의 max값을 출력
    res = 0
    for i in range(n) : 
        res = max(res, dp[i][m-1])
    print(res)