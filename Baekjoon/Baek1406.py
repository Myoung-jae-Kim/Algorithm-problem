#에디터
#명령어 개수 입력받기
from sys import stdin

str = list(stdin.readline().strip())
str1 = []
N = int(stdin.readline())


for i in range(N) :
    command = stdin.readline().split()
    if command[0] == 'P' : 
        str.append(command[1])

    elif command[0] == 'B' : 
        if str : 
            str1.pop()
        else : 
            continue

    elif command[0] == 'D' : 
        if str1 : 
            str.append(str1.pop())
        else :
            continue
    elif command[0] == 'L' :
        if str : 
            str1.append(str.pop())
        else :
            continue

print(''.join(str + list(reversed(str1))))