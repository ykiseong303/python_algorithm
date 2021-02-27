'''
분류 : 그리디 알고리즘
문제 : 세탁소 사장 동혁(백준, 2720)
작성일자 : 2021.02.27
'''

# 거스름 돈의 액수가 주어질때, 이를 최소한의 동전으로 주기
# 테스트 케이스의 수 T와 거스름돈 C를 나타내는 정수가 입력
## 목적 : 거스름돈을 최소한의 동전을 사용해서 주기
## 접근 : 단위가 큰 동전부터 거슬러주기

data = [25, 10, 5, 1]
count = []
T = int(input())
for _ in range(T) :
    change = int(input())
    for coin in data :
        n = change//coin
        change %= coin 
        count.append(n)
    print(*count)
    count.clear()