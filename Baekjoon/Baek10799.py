# Baekjoon 10799번 쇠막대기

iron_bar = list(input())
stack = []
result = 0
#print(iron_bar)

for i in range(len(iron_bar)):
    if iron_bar[i] == '(': #쇠막대기의 시작 부분이 나오면 스택에 추가
        stack.append('(')

    else: #() 가 되면(레이저가 나올 때) 쌓여있는 쇠막대기가 잘리면서 개수 추가
        if iron_bar[i-1] == '(':
            stack.pop()
            result = result + len(stack)

        else:
            stack.pop()
            result += 1

print(result)
