#큐
#명령어 개수 입력받기
from sys import stdin

N = int(stdin.readline())
queue = []

for i in range(N) :
    command = stdin.readline().split()
    if command[0] == 'push' : 
        queue.append(command[1])

    elif command[0] == 'pop' : 
        if queue : #queue 에 값이 존재 하면 FIFO 구조이기에 0번째 pop
            print(queue.pop(0))
        else : 
            print(-1)

    elif command[0] == 'size' : 
        print(len(queue))

    elif command[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
            
    elif command[0] == 'front' :
        if len(queue) == 0 :
            print(-1)
        else : 
            print(queue[0])
    
    elif command[0] == 'back' :
        if len(queue) == 0 :
            print(-1)
        else : 
            print(queue[-1])