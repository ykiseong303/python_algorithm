'''
분류 : 그리디 알고리즘
문제 : 잃어버린 괄호 (백준 1541번)
작성일자 : 2021.03.02
'''
# 양수와 +,-로 이루어진 식을 입력 받는다
## 목적 : 그 식에 괄호를 적절하게 쳐서 연산의 값이 최소화가 되게 만들기
## 접근 : -를 많이 살리기 
##       입력된 식에서 처음으로 -를 만나면 그 이후의 값은 따로 더해놓기

# 다른풀이
# 접근 : 문자열처리ㅔ서 -를 기준으로 split을 시켜준다 
#       그후 다시 +로 split시켜준다
#       분리되는 첫번째 값을 나머지에서 빼주면 끝
math = list(input().split('-'))
print(math)
# plus = math[0]
# math.pop(0)
cur =[]
num = []
for m in math : 
    cnt = 0
    cur = m.split('+')
    for c in cur : 
        cnt += int(c)
    num.append(cnt)
    print(num)
n = num[0]
for i in range(1,len(num)) : 
    n -= num[i]
print(n)



'''
# 직접 풀이 
math = input()
num = 0 
cur = []
real = []
index = 0
for var in math : 
    num = 0
    cur.append(var)
    #print(cur)
    if var == '+' or var == '-' : 
        cur.pop()
        for i in range(len(cur)) : 
            num += int(cur[i]) * (10**(len(cur)-i-1))
        real.append(num)
        #index += len(cur)-1
        real.append(var)
        #index += 1
        cur.clear()

for i in range(len(cur)) : 
    num += int(cur[i]) * (10**(len(cur)-i-1))
real.append(num)
# print(real)
a = 0
b = 0
minus = False
for r in real : 
    if r == '+' : 
        continue
    if r == '-' : 
        minus = True
        continue
    if minus == True : 
        b -= r 
    else : 
        a += r
print(a+b)
'''