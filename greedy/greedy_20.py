'''
분류 : 그리디 알고리즘
문제 : 캠핑 (백준 4796번)
작성일자 : 2021.03.04
'''
# V일의 휴가 중, P일마다 L일씩만 캠핑장을 쓸 수 있다
## 목적 : V일의 휴가중 캠핑장을 사용할 수 있는 최대 일수 출력
## 접근 : 최대로 사용할 수 있는 일수만 우선 구하기
case = 1
while 1 :
    max_vac = 0
    min_vac = 0
    L, P, V = map(int, input().split())
    if V == 0 : 
        break
    max_vac = (V//P)*L
    min_vac = V%P
    if min_vac > L : 
        min_vac = L
    print("Case {}: {}".format(case,max_vac+min_vac))
    case += 1

