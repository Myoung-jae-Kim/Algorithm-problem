#에디터
#명령어 개수 입력받기
from sys import stdin

left = list(stdin.readline().strip())
right = []
N = int(stdin.readline())


for i in range(N) :
    command = stdin.readline()
    if command[0] == 'P' : 
        left.append(command[2])

    elif command[0] == 'B' : 
        if left : 
            left.pop()
        else : 
            continue

    elif command[0] == 'D' : 
        if right : 
            left.append(right.pop())
        else :
            continue
    elif command[0] == 'L' :
        if left : 
            right.append(left.pop())
        else :
            continue

print(''.join(left + list(reversed(right))))