'''
분류 : 그리디 알고리즘
문제 : 아우으 우아으이야!! (백준 15922번)
작성일자 : 2021.02.28
'''

# 수직선 위에 주어진 좌표를 토대로 선분을 그린다
## 목적 : 선분의 길이의 총합을 출력
## 접근 : 정렬후 기준이 되는 x,y사이에 있는 선분 중 가장 길은 선분을 선택
##       접근 방법 알고나면 경우의 수 명확하게 정의하기(구현에 매우 도움)
##       마지막 항의 처리까지 완벽하게 구현하기
N = int(input())
lst = [] 
for _ in range(N) : 
    var = list(map(int, input().split()))
    lst.append(var)

x, y = lst[0][0], lst[0][1]
result = 0
for i in range(1,len(lst)) : 
    temp_x = lst[i][0]
    temp_y = lst[i][1]
    if x<=temp_y<=y: 
        continue 
    elif x<=temp_x<=y and not x<=temp_y<=y : 
        y = temp_y
    else : 
        result += y - x
        x = temp_x
        y = temp_y
print(result+ y - x)













'''
N = int(input())
lst = []
for i in range(N) : 
    point = list(map(int, input().split()))
    lst.append(point)
# print(lst)

start = lst[0][0]
end = lst[0][1]
total = 0
sub_total = 0
for j in range(1,len(lst)) : 
    if start <= lst[j][0] <= end : 
        if end < lst[j][1] : 
            end = lst[j][1] 
            sub_total = abs(end - start)
        if j == len(lst) - 1 : 
            total += abs(end - start)
        # print("if start :", start, "end :",end)
    else : 
        sub_total = abs(end - start)
        # print("sub_total :",sub_total)
        start = lst[j][0]
        end = lst[j][1]
        total += sub_total
        # print("else start :", start, "end :",end)
        if j == len(lst) - 1 : 
            total += abs(end - start)
    
print(total)
'''
