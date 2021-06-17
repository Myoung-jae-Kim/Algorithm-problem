import sys

N = int(sys.stdin.readline())
str_list = []

for _ in range(N):
    str_list = list(map(str, sys.stdin.readline().split()))
    for i in str_list:
        print(i[::-1], end = " ")
    print()
