'''
분류 : 그리디 알고리즘
문제 : 주식 (백준 11501번)
작성일자 : 2021.03.19
'''

# 목적 : 주식을 팔아서 최대 수익 내기
# 접근 : 최댓값이 나타날때 판매하기
#       앞으로 탐색 (시간적 문제, 연산과정), 뒤로 탐색의 응용을 느끼기
#       그래도 문제를 풀면서, 다양한 구현경험 그리고 최대힙을 이용한 방법등을 생각해봄

T = int(input())
for _ in range(T) : 
    N = int(input())
    stock = list(map(int, input().split()))
    target =stock[-1]
    answer = 0
    for i in range(N-2,-1,-1) : 
        if target < stock[i] : 
            target = stock[i]
        else : 
            answer += target - stock[i]
    print(answer)

'''
# 다른풀이 1 
# 앞으로 순회하는 방법 (시간초과)
import sys 
import heapq

T = int(input())
for _ in range(T) : 
    N = int(input())
    stock = list(map(int, sys.stdin.readline().rstrip().split()))
    target = max(stock)
    answer = 0 
    for i in range(len(stock)) : 
        # print(target, stock[i])
        if target == stock[i] : 
            if i == len(stock)-1 :
                break
            # 기존의 최댓값을 지나치고나면 그 이후의 구간에서 새로운 최댓값을 찾음
            temp = stock[i+1:]
            target = max(temp)
        else : 
            # print("answer",answer,"target",target,"stock[i]",stock[i])
            answer += target - stock[i]
            # print("answer",answer)
    print(answer)
'''
'''
T = int(input())
for _ in range(T) : 
    N = int(input())
    stock = list(map(int, sys.stdin.readline().rstrip().split()))
    myQue = []
    answer = 0
    temp = []
    # 주식을 최대힙으로 저장
    for s in stock : 
        heapq.heappush(myQue,-s)
    target = myQue[0] * -1 
    for i in range(len(stock)) : 
        print(stock[i], target)
        if stock[i] == target :
            # 최댓값을 찾으면 현재의 힙에서 최댓값을 빼기 
            if i == len(stock) -1 : 
                break
            # if len(myQue) == 0 : 
            #     break
            heapq.heappop(myQue)
            target = myQue[0] * -1 
            # 최댓값 만난 이후의 리스트에서 새로운 최댓값을 구하기 위해 pop을 진행
            if target in temp : 
                while 1: 
                    if target not in temp : 
                        break
                    heapq.heappop(myQue)
                    target = myQue[0] * -1
            continue
        answer += target - stock[i]
        temp.append(stock[i])
        # 산 주식은 pop 시키기
        # heapq.heappop(myQue.index(stock[i]))
    print(answer)
'''

'''
import sys
T = int(input())
for _ in range(T) : 
    N = int(input())
    stock = list(map(int, sys.stdin.readline().rstrip().split()))
    start = stock[0] 
    temp = []
    temp.append(start)
    answer = 0
    for i in range(1,len(stock)) : 
        num = temp[-1] 
        if num <= stock[i] : 
            temp.append(stock[i])
            # print(temp,i)
            if i == len(stock) -1 : 
                for i in range(len(temp)-1) : 
                    answer += temp[-1] - temp[i]
        else : 
            if len(temp) != 0 : 
                for j in range(len(temp)-1) : 
                    answer += temp[-1] - temp[j]
                temp.clear()
                temp.append(stock[i])
                # print(temp,stock[j],i)
            else : 
                temp.pop()
                temp.append(stock[i])
    # print(temp)
    print(answer)
'''
            
