'''
분류 : 그리디 알고리즘
문제 : 수 묶기 (백준 1744번)
작성일자 : 2021.03.04
'''

# 명확한 조건 추가 필요
# 문제의 보기와 같은 형태라면 맞으나, 특수한 경우 (1,1 or -1,0 등)에는 안맞음
## 목적 : 수를 묶거나 안묶거나 이런 과정을 통해 연산의 최댓값 출력
## 접근 : 음수, 양수 구분없이 가장 큰 수끼리는 곱한다. (0,1은 제외)

N = int(input())
seq = []
for _ in range(N) : 
    seq.append(int(input()))
#seq.sort(reverse=True)
minus = []
minus_cnt = 0
plus = []
zero_one = []
for num in seq : 
    if num < 0 : 
        minus.append(num)
        minus_cnt += 1
    elif num > 1 : 
        plus.append(num)
    else : 
        zero_one.append(num)
total = 1
temp = 0
result = 0
#print(minus)
#if len(minus) != 0 and plus
if not minus_cnt%2 : 
#    if len(minus) == 0 : 
#        total = 0
    minus.extend(plus)
    for num in minus : 
        total *= num
    if total > 1 :
        result = total + sum(zero_one)
else : 
    minus.sort(reverse=True)
    temp = minus[0]
    minus.pop(0)
    minus.extend(plus)
    # print("minus")
    for num in minus : 
        total *= num
        # print("total", total)
        result = total + sum(zero_one) + temp
if len(minus) == 1 and (0 in zero_one): 
    if len(zero_one) == 1 : 
        print(0)
    else : 
        print(1)
elif len(minus) == 0 : 
    print(sum(zero_one))
#print(minus)