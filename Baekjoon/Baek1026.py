#보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

for _ in range(N):
    result += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(result)