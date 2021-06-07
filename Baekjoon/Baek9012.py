#괄호

N = int(input())

for _ in range(N):
    Case = list(input())
    close = 0

    #print(Case)
    while(len(Case) != 0):
        if(close < 0):
            break
        temp = Case.pop()

        if(temp == '('):
            close -= 1
        
        if(temp == ')'):
            close += 1
    
    if(close == 0):
        print('YES')
    else:
        print('NO')
