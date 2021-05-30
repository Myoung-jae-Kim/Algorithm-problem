#덱
#명령어 개수 입력받기
from sys import stdin
from collections import deque

N = int(stdin.readline())
dq = deque()

for i in range(N) :
    command = stdin.readline().split()
    if command[0] == 'push_front' : 
        dq.appendleft(command[1])
    
    elif command[0] == 'push_back' :
        dq.append(command[1])

    elif command[0] == 'pop_front' : 
        if dq :
            print(dq.popleft())
        else : 
            print(-1)

    elif command[0] == 'pop_back' :
        if dq : 
            print(dq.pop())
        else :
            print(-1)

    elif command[0] == 'size' : 
        print(len(dq))

    elif command[0] == 'empty' :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
            
    elif command[0] == 'front' :
        if len(dq) == 0 :
            print(-1)
        else : 
            print(dq[0])
    
    elif command[0] == 'back' :
        if len(dq) == 0 :
            print(-1)
        else : 
            print(dq[-1])