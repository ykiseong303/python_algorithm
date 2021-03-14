'''
분류 : 그리디 알고리즘
문제 : 강의실 배정 (백준 11000번)
작성일자 : 2021.02.26
'''
'''
2021.02.26
- 실패 (시간초과), 로직은 돌아가는 것 같은데 너무 많은 반복문으로 타임아웃인듯? 
- 큐와 그리디 알고리즘으로 문제를 풀기 위한 방법의 숙달이 더 필요할 것 같다
2021.03.14 (2차 풀이)
- 우선순위큐를 이용한 문제 풀이
'''

import heapq 
import sys

## 목적 : 모든 수업을 다 마칠 수 있는 최소한의 강의실 수 
## 접근 : 기준 시간에서 다음에 바로 할 수 있는 강의는 이어서 하기 
##       최소힙을 사용하여 구현
##       시작 시간이 끝나는 시간보다 크면 이어서 할 수 있으므로 pop, 작다면 현재 시간에는 이어서 할 수 없으므로 push

N = int(input())
time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 시작시간을 기준으로 오름차순 정렬
time.sort(key= lambda x:x[0])
# 최소 힙을 사용할 리스트 생성
queue = []
for i in range(N) : 
    if len(queue) != 0 and queue[0] <= time[i][0] : 
        heapq.heappop(queue)
    heapq.heappush(queue,time[i][1])
print(len(queue))



'''
# S(i)에 시작해서 T(i)에 끝나는 N개의 수업이 주어짐
# 수업이 끝난 직후에 다음 수업을 할 수 있다. 
# > (1, 3), (3, 5) 사이에 (2, 4)의 수업은 진행할 수 없다
# > 1,3-3,5는 같은 강의실에서, 2-4는 다른 강의실에서 진행
# 첫 줄에 수업의 수 N, 이후 N개의 줄에 S(i)와 T(i)가 입력된다.
## 문제의 목적 : N개의 수업은 무조건 끝내야 하는데, 강의실은 최소한으로 사용
## 문제의 풀이 : 시작시간 - 끝시간이 0이거나 가장 작은 양수일때를 찾기,
##             나머지는 그 시간에 못하니깐 다른 강의실로 배정
import sys
N = int(input())
time = []
for _ in range(N) : 
    s = map(int, sys.stdin.readline().rstrip().split())
    #s = list(map(int, input().split()))
    time.append(s)
print(s)
count = 0 
cur = [] 
while len(time) > 1 : 
    target = time[0][1]
    time.pop(0)
    minus_count = 0
    for i in range(len(time)) : 
        if target <= time[i][0] : 
            target = time[i][1]
            time[i][1] = -1
            minus_count += 1

        if i == len(time)-1 : 
            index = 0
            while index < minus_count : 
                for j in range(len(time)) : 
                    if time[j][1] == -1 : 
                        time.pop()
                        break
                index += 1
    count += 1
print(count+1)
'''



