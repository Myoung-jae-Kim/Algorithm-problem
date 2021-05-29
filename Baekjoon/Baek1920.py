#수 찾기
from sys import stdin

def binary_search(Num_list,Num):
    low = 0
    high = len(Num_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if (Num_list[mid] == Num):
            return 1 
        elif (Num_list[mid] < Num):
            low = mid + 1
        else:
            high = mid - 1
    return 0

N = int(stdin.readline())
N_list = list(map(int, input().split()))

M = int(stdin.readline())
M_list = list(map(int, input().split()))

#이진탐색을 위한 리스트 정렬
N_list.sort()

for i in range(M):
    print(binary_search(N_list,M_list[i]))
        
    