#회의실배정
#회의가 겹치지 않도록 최대 회의실의 개수 구하기

Meeting_Count = int(input())
Meeting_Room = 0
end_time = 0
Meeting = []

for i in range(Meeting_Count):
    start, end = map(int, input().split())
    Meeting.append((start, end))

#시작시간 기준으로 정렬
Meeting = sorted(Meeting, key=lambda time: time[0])
#종료시간 기준으로 정렬
Meeting = sorted(Meeting, key=lambda time: time[1])

#시작시간이 끝나는 시간 보다 크거나 같을 경우 회의실이 1개 더 필요함
for i, j in Meeting:
    if i >= end_time:
        Meeting_Room += 1
        end_time = j

print(Meeting_Room)
