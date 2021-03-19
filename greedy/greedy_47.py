'''
분류 : 그리디 알고리즘
문제 : 폴리오미노 (백준 1343번)
작성일자 : 2021.03.19
'''

# 목적 : 폴리오미노로 모두 덮은 보드판을 출력한다 
# 접근 : 가장 많이 덮을 수 있는 것부터 처리한다 
#       예외 조건을 고려한다 (X가 홀수개, .이 두개이상, .이 맨 앞에 나오는 경우)

# 다른풀이 1 
# replace를 사용한다
# 긴 것부터 없애야하는 그리디를 적용하여 AAAA변환을 먼저 수행한다 
board = input()
# 문자열의 왼쪽부터 replace를 수행한다 
board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')
# 모두 바꾸고 난뒤에도 X가 남아있다면 출력불가
if 'X' in board : 
    print(-1)
else : 
    print(board)

'''
import sys

lst = input()
temp = []
count = 0
dot_count = 0
if lst[0] == '.' : 
    x = False 
else : 
    x = True
for i in range(len(lst)) : 
    if lst[i] == 'X' : 
        x = True
        # temp.append(dot_count)

        count += 1
    if x==True  and (lst[i] == '.' or i == len(lst) -1) : 
        x = False 
        if count % 2 : 
            print(-1)
            sys.exit()

        temp.append(count)
        count = 0
        dot_count += 1 
# print(temp)
flag = True
for l in lst : 
    if l=='X' and flag ==True : 
        flag = False
        for i in range(len(temp)) : 
            if temp[i] == 2 : 
                print("BB",end='')
                temp.pop(i)
                break
            else : 
                for _ in range(temp[i]//4) : 
                    print("AAAA",end='')
                if temp[i]%4 : 
                    print("BB",end='')
                temp.pop(i)
                break
    if l=='.' : 
        print(l,end='')
        flag = True
'''

