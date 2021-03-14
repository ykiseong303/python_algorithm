'''
분류 : 그리디 알고리즘
문제 : 회의실 배정 (백준 1931번)
작성일자 : 2021.03.01
'''
'''
2021.03.14 (2차 풀이)
- 정렬을 이용한 풀이
'''
# 시작과 끝 시간이 다른 회의가 N개 있음
## 목적 : 1개의 회의실에 사용할 수 있는 최대의 회의 갯수 출력
## 접근 : 시작 시간도 짧고, 끝나는 시간도 짧은 순으로 정렬 
##       왜 두번 하냐면, (3,4) > (2,4)의 순서로 입력받을 경우 끝나는 순으로만 정렬하면 
##       기존의 순서를 그대로 유지하려 하기 때문에 (2,4)의 우선순위가 높음에도 무시될 수 있음

import sys

N = int(input())
time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 시작 시간과 끝나는 시간의 순서로 오름차순 정렬
time.sort(key= lambda x:(x[1],x[0]))
# for t in time : 
#     print(*t)
start = time[0][1]
count = 1
for i in range(1,N) : 
    if start <= time[i][0] : 
        count += 1 
        start = time[i][1]
print(count)














'''
import sys
N = int(input())
time = []
for _ in range(N) : 
    #a = list(map(int, input().split()))
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    time.append(a)
time.sort(key= lambda x: x[0])
time.sort(key= lambda x: x[1])
j = 0
count = 0
result = 0
if len(time) == 1 : 
    print(1)
else : 
    while j != len(time) - 1 : 
        #print("while")
        target = time[j][1] - time[j][0]
        for i in range(j,len(time)) : 
            # #print(j)
            # if j == len(time) -1 : 
            #     print("j")
            #     break
            if result > time[j+1][0] : 
                j += 1 
                break
            cur = time[i+1][1] - time[i+1][0]
            if target > cur : 
                count += 1
                result = time[i+1][1]
                j += 1
                #print(result)
            else : 
                count += 1 
                result = time[i][1]
                j += 1
                #print(result)
    print(count)
'''



'''
result = 0
count = 0
escape = 0
while 1: 
    #print(time)
    #print(count)
    for i in range(1,len(time)) : 
        if result > time[i][0] : 
            target_point += 1
            break
        target = time[0][1] - time[0][0]
        target_point = 0
        cur = time[i][1] - time[i][0]
        if  cur < target : 
            result = time[i][1]
            target_point = i
            count += 1
            print("[",time[i][0],time[i][1],"]")
        else : 
            result = time[0][1]
            count += 1
            print("[",time[0][0], time[0][1],"]")
    time = time[target_point:]
    if len(time) == 1 : 
        break
print(count)

'''