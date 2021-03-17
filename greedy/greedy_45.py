'''
분류 : 그리디 알고리즘
문제 : 사과 담기 게임 (백준 2828번)
작성일자 : 2021.03.17
'''

# 목적 : 사과를 모두 담을 수 있는 바구니의 최소 이동횟수
# 접근 : 먼저 떨어지는 사과부터 받기 
#       바구니의 범위를 명확하게 지정

N, M = map(int, input().split())
J = int(input())
apple = [int(input()) for _ in range(J)]
start = 0
cnt = 0
for a in apple : 
    # print(a)
    if start< a and a<=start+M : 
        # print("stay",start, start+M, a)
        continue
    elif start+M < a : 
        while 1: 
            start += 1 
            cnt += 1 
            if start < a and a <= start+M : 
                # print("right",start, start+M, a)
                break
        continue
    elif a <= start : 
        while 1 : 
            start -= 1 
            cnt += 1 
            if start<a and a<=start + M : 
                # print("left",start, start+M, a)
                break
        continue
print(cnt)