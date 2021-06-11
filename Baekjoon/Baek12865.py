#평범한 베낭

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k + 1):
        if weight > j:  # 현재 아이템의 무게가 현재 채우는 가방의 무게 보다 크면 덮어씀.
            dp[i][j] = dp[i - 1][j]
        else:
            # i번째 아이템을 챙겼을 때 갖는 최댓값과 i번째 아이템을 챙기지 않았을 때의 최댓값중 큰 값을 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])