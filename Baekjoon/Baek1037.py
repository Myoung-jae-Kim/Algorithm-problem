#약수
#양수 A가 N의 약수가 되려면 N은 A의 배수, 1 < A < N, N의 진짜 약수가 모두 주어질 때 N을 구하는
#N의 진짜 약수의 개수 50보다 작거나 같은 수, 둘째 줄에는 진짜 약수들


Num = int(input()) # 약수 개수
dd = list(map(int,input().split())) #진짜 약수들

max = max(dd)
min = min(dd)

print(max*min)