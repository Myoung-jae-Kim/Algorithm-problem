#저울 주어진 추 들로 측정할 수 없는 양의 정수 무게 중 최솟값 구하기

num = int(input())
w = list(map(int, input().split()))
w.sort()
result = 1

for i in range(len(w)):
    if result < w[i]:
        break
    result += w[i]

print(result)