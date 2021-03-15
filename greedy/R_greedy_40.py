'''
분류 : 그리디 알고리즘
문제 : 센서 (백준 2212번)
작성일자 : 2021.03.15
'''

# 직선상의 도로에 N개의 센서가 있고, 이를 수신할 수 있는 집중국 K개를 설치한다
# 모든 센서는 1개 이상의 집중국 수신 영역에 들어야 한다 
## 목적 : 집중국이 수신할 수 있는 거리들의 최솟값을 출력 
## 접근 : K개의 집중국의 수신영역이 모두 비슷해질 수 있는 포인트를 찾는다 
##       문제의 경우의 수를 생각해보기 (간격이 모두 같은경우)

import sys

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

# 센서의 수가 집중국 수보다 적다면 그 위에 설치하면 되므로 거리는 0이된다
if N<=K : 
    print(0)
    # 이후 내용은 실행하지 않고 종료
    sys.exit()
# 센서의 위치를 오름차순으로 정렬한다
sensor.sort()
# 센서들의 격차를 저장할 리스트 생성
distance = []
# 센서들의 격차를 distance에 저장한다
for i in range(len(sensor)-1) : 
    distance.append(sensor[i+1]-sensor[i])
# 격차 리스트를 내림차순으로 정렬한다
distance.sort(reverse=False)
# 격차 리스트에서 가장 큰 값을 K-1번 pop 시킨다 
for _ in range(K-1) : 
    distance.pop()
print(sum(distance))