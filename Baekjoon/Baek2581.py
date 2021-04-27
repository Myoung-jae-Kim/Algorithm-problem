#소수

M = int(input())
N = int(input())

sosu_list = []
for i in range(M, N+1):
    error = 0
    if i > 1 :
        for j in range(2, i):  # 2부터 i-1까지
            if i % j == 0:
                error += 1
                break  # 2부터 i-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(i)  # error가 없으면 소수리스트에 추가

if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)