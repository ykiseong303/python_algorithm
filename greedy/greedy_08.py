'''
분류 : 그리디 알고리즘
문제 : 스네이크버드 (백준 16435번)
작성일자 : 2021.02.27
'''

# 스네이크 버드는 자신의 길이보다 작거나 같은 높이의 과일을 먹을 수 있다
# 과일 하나를 먹을 때 마다 길이가 1만큼 늘어나게 된다 
## 목적 : 주어진 과일을 다 먹었을 때 최대 길이를 출력
## 접근 : 현재 크기보다 작은 것들을 다 먹고 이후의 것들을 먹으려고 시도한다
'''
a, b = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

for i in c : 
    if b >= int(i) : 
        b += 1
print(b)
'''
import sys

lst = []
for i in range(2):
    a = sys.stdin.readline().rstrip()
    lst.append(list(map(int, a.split())))
    print(lst)
lst[1].sort()

init = int(lst[0][1])
for i in lst[1]:
    if init >= int(i):
        init += 1
print(init)
