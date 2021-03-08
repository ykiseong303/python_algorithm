'''
분류 : 그리디 알고리즘
문제 : 보석도둑 (백준 1202번)
작성일자 : 2021.03.07
'''

# 보석은 가격과 무게 정보를 갖고 있고, 가방에 담을 수 있는 최대 무게가 존재
# 가방에는 1개의 보석만 넣을 수 있다
## 목적 : 훔칠 수 있는 보석 가격의 합의 최댓값을 출력
## 접근 : 가장 가볍고 가장 비싼 보석부터 처리한다 
##       최대 무게가 가장 가벼운 가방에 비싼 보석을 넣는 것을 우선으로 생각
##       이중 반복문을 통한 O(N^2)을 피하도록 구현 

# 가방을 오름차순으로 정렬한다 (정렬하지 않으면 밑의 while조건문에서 문제 발생)
## 기준이 되는 가방보다 작거나 같은 보석이 다 들어가야하는데, 못들어가는 경우 생김
# 보석을 무게를 기준으로 오름차순 정렬한다 
# 반복문(가방기준)을 돌며 현재 가방무게보다 작거나 같은 보석을 최대힙에 넣는다 
## 최대힙에는 보석의 가격을 넣는다 
## 중요한 점은 특정 가방의 무게보다 작거나 같아서 들어간 보석은 어차피 추후에 다른 가방에도
## 들어가지므로, 최대힙으로 큰 값들만 빼주면 된다
import sys
import heapq

N, K = map(int, input().split())
jew = []
bag = []
for _ in range(N) : 
    jew.append(list(map(int, sys.stdin.readline().rstrip().split())))
jew.sort(key= lambda x: x[0])
for _ in range(K) : 
    bag.append(int(sys.stdin.readline().rstrip()))
bag.sort()

myQue = []
index = 0
result = 0
### 기준을 남긴채로 반복문 돌리는 기법 (단순 이중 for문과의 차이)
for i in range(len(bag)) : 
    # 기준이 되는 가방보다 무게가 작은 보석들을 집어넣기
    # while 반복문의 탈출조건
    ## 파이썬은 인터프리터 언어이므로 로직상으로 맞아도 순서에 따라 틀려질 수 있음
    ## index<N이 and뒤에 있으면 앞에조건에서 jew의 인덱스를 조회하게 되므로 
    ## 오류가 발생함
    while index<N and bag[i] >= jew[index][0]: 
        # 최대힙으로 대입
        heapq.heappush(myQue, -jew[index][1]) 
        index += 1 
        
    # 기준에 충족하는 보석을 다 채웠으면, 가장 큰 값 비우기
    if len(myQue) : 
        result += heapq.heappop(myQue)
print(-result)


