#숫자 카드2
from sys import stdin

N = int(stdin.readline())
N_list = list(map(int, input().split()))

M = int(stdin.readline())
M_list = list(map(int, input().split()))
hashmap = {}

for i in N_list:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M_list))
    