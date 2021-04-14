#주유소
#1키로당 1리터의 기름을 사용하며, 제일 오른쪽 도시까지 이동 최소 비용 계산.

City = int(input()) #도시의 개수
Distance = list(map(int, input().split())) # 도시 사이의 거리
Cost = list(map(int, input().split())) #도시의 기름 가격
price = 0 #지불할 값

#처음 이동할 때 드는 기름 값은 첫번째 도시의 기름값*다음 도시까지 거리
Cost_Vs = Cost[0]

#마지막 도시에 도착하면 기름값 계산 필요없으니 최종 거리까지만 비교
for i in range(len(Distance)):
    if Cost[i] <= Cost_Vs:
        Cost_Vs = Cost[i]
        price += Distance[i]*Cost_Vs
    else:
        #기름값이 다음 주유소기름값 보다 작을 때 거리만큼 더 충전
        price += Distance[i]*Cost_Vs
        continue
  
print(price)