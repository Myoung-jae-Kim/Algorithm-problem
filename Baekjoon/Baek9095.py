import sys

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

T = int(sys.stdin.readline())
for _ in range(T):
    print(sol(int(sys.stdin.readline())))