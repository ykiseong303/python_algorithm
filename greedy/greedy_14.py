'''
분류 : 그리디 알고리즘
문제 : 동전 0 (백준 11047번)
작성일자 : 2021.03.01
'''

# 목적 : 최소한의 동전 개수 출력
# 접근 : 최대한 나누되, 못나누면 빼야지
## 입력 받는 속도도 감안하기
import sys
N, K = map(int, input().split())
money = []
for _ in range(N) : 
    a = int(sys.stdin.readline().rstrip())
    money.append(a)

count = 0
money.reverse()
for coin in money : 
    if coin <= K : 
        if not K%coin : 
            count += K//coin
            K = K%coin

        else : 
            while 1 : 
                K = K - coin
                count += 1
                if K < coin : 
                    break
print(count)