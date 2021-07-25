#후위 표기식2

N = int(input())
S = input()
a = [0] * N

for i in range(N):
    a[i] = int(input())

stack = []

for i in S:
    if 'A' <= i <= 'Z':
        stack.append(a[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' %stack[0])