#로프
#각 로프가 버틸 수 있는 최대 중량이 주어지는데 이로프를 이용하여 들어올릴 수 있는 최대 중량

low = int(input())
low_w = []
total = []

#w = int(int())
#w = [int(input()) for i in range(N)]

for i in range(low):
    low_w.append(int(input()))

low_w.sort(reverse=True)

# 로프의 중량 * 로프의 갯수 각 수를 비교해서 제일 큰 값이 최대 중량
for i in range(low):
    total.append(low_w[i]*(i+1))

print(max(total))


#print(low_w[0], low_w[1])

# bow = int(input()) # 활잡이 수
# top = list(map(int,input().split())) # 봉우리 수

# ans = 0
# maxhill = 0
# cnt = 0

# for hill in top:
#     if hill > maxhill:
#         maxhill = hill
#         cnt = 0
#     else:
#         cnt +=1
#     ans = max (ans, cnt)

# print(ans)
