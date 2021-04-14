#블랙잭
#카드의 합이 21을 넘지 않는 선에서 카드의 합을 최대한 크게 만드는 게임 N장 중 3장을 고르고 딜러가 외친 M의 합에 가깝게 만들어라

N, M = map(int, input().split())
Number = list(map(int, input().split()))
Sum = 0

Number.sort(reverse=True) #가장 큰수가 먼저 오게끔 내림차순

for i in range(len(Number)):
    for j in range(i+1,len(Number)):
        for k in range(j+1,len(Number)):
            if Number[i] + Number[j] + Number[k] > M:
                continue
            else:
                Sum = max(Sum, Number[i] + Number[j] + Number[k])
print(Sum)
