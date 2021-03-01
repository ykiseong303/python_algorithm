'''
분류 : 그리디 알고리즘
문제 : 피보나치 (백준 9009번)
작성일자 : 2021.02.27
'''

# 하나의 양의 정수에 대한 피보나치 수들의 합은 여러 가지 형태가 있다
# 하나의 양의 정수를 최소 개수의 서로 다른 피보나치 수들의 합으로 나타내기
## 목적 : 피보나치 수들의 합이 주어진 정수와 같게 되는 최소수의 수열 출력
## 접근 : 피보나치 수열의 각 원소들의 합으로 최대한 크게 만들기 ! 
'''
lst = [1,2]
def fi(a1, a2,n) : 
    if n == 50 : 
        #print(lst)
        return lst
    swap = a1
    a1 = a2
    a2 = a1 + swap 
    lst.append(a2)
    n += 1
    fi(a1,a2,n)
fi(1,2,1)
# print(lst)
'''
lst=[1,2]
for i in range(2,46):
    lst.append(lst[i-1]+lst[i-2])
n = int(input())

for i in range(n) : 
    num = int(input())
    result = []
    for j in range(len(lst)) :
        if lst[45-j] <= num : 
            result.append(lst[45-j])
            num -= lst[45-j]
    result.sort()
    print(*result)
'''
        if lst[51-j] < num : 
            result.append(lst[51-j])
            num -= lst[51-j]
        if num == 3 : 
            result.append(3)
            break
        if num == 1: 
            result.append(1)
            break

    result.reverse()
    print(*result)
'''

