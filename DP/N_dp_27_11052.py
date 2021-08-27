'''
분류 : 다이나믹 프로그래밍
문제 : 카드 구매하기 (백준 11052)
작성일자 : 2021.07.10 
'''

# 목적 : N개의 카드를 최대 금액으로 구입하는 금액 출력
# 접근 : dp

N = int(input())
lst = [0] + list(map(int, input().split())) 
d = [0] * (N+1)
d[1] = lst[1] 
for i in range(2, N+1) :  
    for j in range(1,i+1) : 
        if d[i] < d[i-j] + lst[j] : 
            d[i] =  d[i-j] + lst[j]
print(d[N])
