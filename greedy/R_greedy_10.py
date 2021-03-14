'''
분류 : 그리디 알고리즘
문제 : 통나무 건너뛰기 (백준 11497번)
작성일자 : 2021.02.27
'''
'''
2021.03.14 2차풀이
'''

# 통나무 건너뛰기를 하는데, 인접한 각 통나무의 높이 차가 최소가 되도록 놓는다
# 인접한 것중 가장 차이가 큰 것을 난이도로 지정한다
## 목적 : 난이도가 최소가 되도록 출력
## 접근 : 인접한 통나무들의 높이 차가 최소가 되도록 정렬 
##       높이가 가장 큰 통나무가 중간에 오도록 인덱스의 차이를 2로 둔다 

T = int(input())
for i in range(T) : 
    N = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    result = 0
    for j in range(2,len(trees)) : 
        result = max(result, trees[j]-trees[j-2])
    print(result)