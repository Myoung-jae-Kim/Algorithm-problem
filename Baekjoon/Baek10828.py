#스택
#명령어 개수 입력받기
from sys import stdin

N = int(stdin.readline())
stack = []

for i in range(N) :
    command = stdin.readline().split()
    if command[0] == 'push' : 
        stack.append(command[1])

    elif command[0] == 'pop' : 
        if stack : #stack 에 값이 존재 하면 FILO 구조이기에 List에 마지막 값 출력
            print(stack.pop(len(stack)-1))
        else : 
            print(-1)

    elif command[0] == 'size' : 
        print(len(stack))

    elif command[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
            
    elif command[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else : 
            print(stack[-1])