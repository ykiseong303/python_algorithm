'''
분류 : 그리디 알고리즘
문제 : 공항 (백준, 107745번)
작성일자 : 2021.03.11
'''

# G개의 게이트에 i번째 비행기를 1번부터 Gi번째 게이트 중에 도킹
## 목적 : 최대로 도킹시킬 수 있는 비행기의 수 출력
## 접근 : Gi번째 게이트 중 가장 숫자가 큰 게이트에서부터 차례로 도킹한다
##       밑의 두가지 방법으로도 가능하지만(시간초과) 유니온-파인드 자료구조 숙달이 필요

import sys
G = int(input())
P = int(input())
planes = []
gate = [0 for _ in range(G)]
for _ in range(P) : 
    planes.append(int(sys.stdin.readline().rstrip()))

flag = True
count = 0
temp = []
max_var = 0
for plane in planes : 
    if flag == False : 
        break
    if gate[plane-1] == 0 : 
        gate[plane-1] = plane
        count += 1
    else : 
        # print("else", plane)
        temp = gate[:gate.index(max(gate))+1]
        max_temp = gate[gate.index(max(gate))+1 : ]
        temp.reverse()
        try : 
            if temp.index(0) : 
                temp[temp.index(0)] = plane
                temp.reverse()
                temp.extend(max_temp)
                gate = temp
                count += 1
        except : 
            # print("flag :",flag)
            flag = False 
'''
# 다른 풀이
        # print("else", plane)
        while 1 : 
            plane -= 1 
            if plane == 0 : 
                flag = False 
                # print("flag :",flag)
                break
            if gate[plane-1] == 0 : 
                gate[plane-1] = -1
                count += 1
                break 
'''

    # print(gate)
print(count)