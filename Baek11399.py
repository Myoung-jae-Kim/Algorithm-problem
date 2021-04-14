#ATM
#각 사람이 돈 인출하는 시간의 최소 합 구하기

#사람 수 만큼의 배열에서 오름 차순 정렬 후 각 배열 시간 더하면 최솟값

People = int(input())
Atm_time = list(map(int, input().split()))
total_time = 0

Atm_time.sort()
# 1
# 1+2
# 1+2+3
# 1+2+3+3
# n*Atm_time[0] + (n-1)*Atm_time[1] ....
for i in range(len(Atm_time)):
    total_time += ((len(Atm_time)) - i)*Atm_time[i]

print(total_time)


