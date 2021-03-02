'''
분류 : 그리디 알고리즘
문제 : 신입사원 (백준 1946번), 나중에 재풀이 필요
작성일자 : 2021.03.02
'''

# 각 사람별 두개의 순위가 주어져 있다
# 순위가 적어도 하나가 다른 사람보다 떨어지지 않는 사람만 채용한다
## 목적 : 최대로 뽑을 수 있는 사원의 수 출력
## 접근 : 두개의 순위가 모두 높은 사람부터 선택 
##       둘 중 하나라도 떨어지지 않는 사람의 조건을 명확히 이해해야 함
##       뽑을 수 있는 경우 중, 최대로 뽑을 수 있는 경우라고 생각하면 됌

import sys
T = int(input())
for _ in range(T) : 
    N = int(input())
    test = []
    count = 1
    for _ in range(N) : 
        a = list(map(int, sys.stdin.readline().rstrip().split()))
        test.append(a)
    test.sort(key=lambda x:x[0])
    best = test[0][1]
    for i in range(1,len(test)) : 
        if best > test[i][1] : 
            count += 1 
            best = test[i][1]
    print(count)

