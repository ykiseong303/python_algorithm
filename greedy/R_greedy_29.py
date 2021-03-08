'''
분류 : 그리디 알고리즘
문제 : 뒤집기(백준 1439번)
작성일자 : 2021.03.08
'''

# 0과 1을 뒤집어서 모두 같은수로 만들기 
## 목적 : 같은 수로 만들기 위해 사용되는 최소 뒤집기의 
## 접근 : 중복된 문자를 제거하면 0과 1의 개수가 각각의 수로 뒤집어야 할 수임
##       001100 은 010과 같음

num = input()
result = []
start = num[0]
result.append(start)
for i in range(1,len(num)) :
    # start = num[i]
    if start != num[i] : 
        result.append(num[i])
        start = num[i]
zero = result.count('0')
one = result.count('1')
print(min(zero,one))

'''
num = input()
zero = num.count('0')
one = num.count('1')
if zero > one : 
    start = '0'
else : 
    start = '1'
temp = start
count = 0
for i in range(len(num)) : 
    if start != num[i] :
        temp = num[i]
        if i == len(num) -1 : 
            count += 1
    if start == num[i] and temp != num[i] : 
        count += 1
        temp = start
print(count)
'''