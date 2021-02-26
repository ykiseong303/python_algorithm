'''
분류 : 그리디 알고리즘
문제 : 강의실 배정 (백준 11000번)
작성일자 : 2021.02.26
'''
'''
2021.02.26
- 실패 (시간초과), 로직은 돌아가는 것 같은데 너무 많은 반복문으로 타임아웃인듯? 
- 큐와 그리디 알고리즘으로 문제를 풀기 위한 방법의 숙달이 더 필요할 것 같다
'''

# S(i)에 시작해서 T(i)에 끝나는 N개의 수업이 주어짐
# 수업이 끝난 직후에 다음 수업을 할 수 있다. 
# > (1, 3), (3, 5) 사이에 (2, 4)의 수업은 진행할 수 없다
# > 1,3-3,5는 같은 강의실에서, 2-4는 다른 강의실에서 진행
# 첫 줄에 수업의 수 N, 이후 N개의 줄에 S(i)와 T(i)가 입력된다.
## 문제의 목적 : N개의 수업은 무조건 끝내야 하는데, 강의실은 최소한으로 사용
## 문제의 풀이 : 시작시간 - 끝시간이 0이거나 가장 작은 양수일때를 찾기,
##             나머지는 그 시간에 못하니깐 다른 강의실로 배정

N = int(input())
time = []
for _ in range(N) : 
    s = list(map(int, input().split()))
    time.append(s)
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
        



