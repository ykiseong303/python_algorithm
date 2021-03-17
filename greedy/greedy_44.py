'''
분류 : 그리디 알고리즘
문제 : 과제 (백준 13904번)
작성일자 : 2021.03.17
'''

# 목적 : 마감기한에 맞춰서 할 수 있는 과제 점수의 최댓값 출력
# 접근 : 마감시간이 가장 빠른 것부터 하되, 나중에 더 큰 값이 있으면 바꿔주기 
#       그리디 알고리즘에서는 나중에 더 좋은 걸로 바꿔줄 수 있다는 점 고려하기 
import sys 

N = int(input())
subject = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
subject.sort(key=lambda x:x[0])
temp = []
day = 0
for sub in subject : 
    if day < sub[0] :
        temp.append(sub[1])
        day += 1 
    else : 
        if min(temp) < sub[1] : 
            temp[temp.index(min(temp))] = sub[1]
print(sum(temp))



'''
import heapq
import sys
N = int(input())
subject = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
subject.sort(key=lambda x:x[1],reverse=True)
result = []
for i in range(len(subject)) : 
    if subject[i][0] > 0 : 
        result.append(subject[i][1])
        for j in range(i+1,len(subject)) : 
            subject[j][0] -= 1 
    print(result)
'''