import sys

N = int(sys.stdin.readline())
num = 2

while True:
    if N % num == 0:
        print(num)
        N //= num
    elif N == 1:
        break
    else:
        num += 1