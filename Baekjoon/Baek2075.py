#N번째 큰 수
import sys
import heapq

N = int(input())
N2list = []
result = []

for _ in range(N):
    N2list = list(map(int, sys.stdin.readline().split()))

    if result:
        for i in N2list:
            if result[0] < i:
                heapq.heappush(result, i)
                #print(result)
                heapq.heappop(result)
                #print(result)
    
    if not result:
        for i in N2list:
            heapq.heappush(result, i)
            #print(result)



#print(N2list)

# for i in range(N):
#     for j in range(N):
#         result.append(N2list[i][j])

#result.sort()

#print(result)
print(result[0])