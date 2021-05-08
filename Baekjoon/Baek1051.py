F = []
N, M = map(int, input().split(' '))
SIZE = 0

for i in range (N):
    F.append(list(map(int, input())))

    SIZE = min(N, M)
    max = 0

for i in range(N):
    for j in range(M):
        for k in range(SIZE):
             if i + k < N and j + k < M:
                 if F[i][j] == F[i][j+k] and F[i][j] == F[i+k][j] and F[i][j] == F[i+k][j+k] :
                    if max < k:
                         max = k


print((max+1)*(max+1))