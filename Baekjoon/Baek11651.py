#좌표 정렬하기2
import sys

N = int(sys.stdin.readline())
result = []

for i in range(N):
    result.append(list(map(int, sys.stdin.readline().split())))


result.sort(key=lambda x : (x[1], x[0]))

#print(result)

for j in result:
    print(j[0], j[1])