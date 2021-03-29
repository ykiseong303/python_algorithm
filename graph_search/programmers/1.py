'''
분류 : 깊이/너비우선 탐색 
문제 : 타겟 넘버 (프로그래머스)
작성일자 : 21.03.28
'''

# 목적 : 주어진 리스트로 타겟 넘버를 만들 수 있는 모든 경우의 수를 출력
# 접근 : 큐를 두개 사용하여 새로운 연산이 추가될때 다른 큐에 집어 넣는다

from collections import deque
lst = list(map(int ,input().split()))

start = lst[0]
q = deque([start])
q.append(-start)
# print(q)
w = deque()
count = 0
target = 3
for i in range(1,len(lst)) : 
    while q  :
        x = q.popleft()
        w.append(x-lst[i])
        # print(x,"-",lst[i])
        w.append(x+lst[i])
        # print(x,"+",lst[i])
    q = w
    w = deque()
    # print(q)
for s in q : 
    if s == target : 
        count +=1 
print(count)