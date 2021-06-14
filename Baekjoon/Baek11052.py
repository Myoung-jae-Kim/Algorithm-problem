#카드 구매하기
import sys

N = int(sys.stdin.readline()) #구매하고자 하는 카드의 개수
P = [0] + list(map(int,sys.stdin.readline().split())) #카드가 i개 들어있는 카드팩 가격
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[i])
    