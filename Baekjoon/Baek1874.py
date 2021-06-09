import sys

n = int(sys.stdin.readline())
stack = []
result = [] #부호를 저장하는 리스트
number = 1
possible = True

for _ in range(n):
    index = int(sys.stdin.readline())
    while number <= index:
        stack.append(number)
        result.append('+')
        number += 1
    
    if stack[-1] == index: #스택의 최상단값이 index 같을 때
        stack.pop()
        result.append('-')
    else:
        possible = False
        
if possible == False:
    print('NO')
else:
    for i in result:
        print(i)