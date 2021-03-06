'''
분류 : 그리디 알고리즘
문제 : 주유소 (백준, 13305번)
작성일자 : 2021.03.06
'''

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동한다 
# 각 도시별로 주유소가 있고, 요금이 다르다 
## 목적 : 제일 오른쪽 도시로 이동하는 가장 적은 비용
## 접근 : 요금이 가장 저렴한 곳에서 다 채운다는 생각으로 ~ 

import sys

N = int(input())
fee = []
distance = []
distance = (list(map(int,(sys.stdin.readline().rstrip().split()))))
fee = (list(map(int,(sys.stdin.readline().rstrip().split()))))
start = fee[0]
total = 0
#print(fee)
for i in range(1,len(fee)) : 
    #print("i",i)
    if i == len(fee) : 
        continue
    if start > fee[i] : 
        total += start * distance[i-1]
        start = fee[i]
        #print("start",start)
    else : 
        #print("else",i)
        total += start * distance[i-1]
        #print("dis",distance[i-1])
    #print(total)
print(total)
        