'''
분류 : 그리디 알고리즘
문제 : ATM (백준 11399번)
작성일자 : 2021.02.27
'''

# 사람들이 줄을 서는 순서에 따라 돈을 인출하느 시간의 합이 달라진다
## 목적 : N명의 사람이 돈을 인출하는데 걸리는 시간의 합의 최소값을 출력 (마지막 사람까지)
## 접근 : 가장 빨리 끝나느 사람부터 끝내기(제일 오래 걸리는 사람을 뒤로 보내기)
##       오래 걸리는 사람이 중간에 껴있으면 끝날때까지 계속 영향을 미침

N = int(input())
person = list(map(int, input().split()))
person.sort()
cur = 0
total = []
for i in person : 
    cur += i
    total.append(cur)
print(sum(total))
