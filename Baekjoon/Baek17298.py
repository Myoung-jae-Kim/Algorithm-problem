#Baekjoon 17298번 오큰수

import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(N)]

for i in range(len(nums)):
    #스택이 비지 않았으면서, 다음수가 해당수보다 크면
    while len(stack)!=0 and nums[stack[-1]] < nums[i]:
        #ans[(stack.pop()=현재 수에 해당하는 인덱스)]배열에 다음수 집어넣기
        ans[stack.pop()] = nums[i]
    stack.append(i)

#print(*ans)

for i in range(N):
    print(ans[i], end = " ")