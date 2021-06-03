#동전1
from sys import stdin

N, K = map(int, stdin.readline().split())
coin = []
dp = [0] * (K+1)
dp[0] = 1

for _ in range(N):
    coin.append(int(stdin.readline()))


for i in coin:
    for j in range(i, K + 1):
        dp[j] += dp[j-i]

print(dp[K])