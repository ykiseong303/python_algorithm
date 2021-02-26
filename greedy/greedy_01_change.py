'''
분류 : 그리디 알고리즘
문제 : 거스름돈 (백준 5585번)
작성일자 : 2021.02.26
'''
# 1000엔 지폐를 냈을 때, 받을 잔돈의 개수
# 거스름돈의 개수는 가장 적어야 한다
# 지불할 돈 1개가 입력된다
## 문제의 목적 : 거스름돈을 최대한 적게 주기 
## 문제의 풀이 : 가장 큰 돈부터 주면 된다

money = [500,100,50,10,5,1]
change = 1000 - int(input())
count = 0
for i in money : 
    count += change//i 
    change = change%i
    if change == 0 : 
        print(count)
        break 
    
