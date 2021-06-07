#중복 빼고 정렬하기

N = int(input())
data = list(map(int,input().split()))


data = list(set(data))
data.sort()

for i in data:
    print(i, end = ' ')