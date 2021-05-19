#성적 통계

class_num = int(input())

result = []

for _ in range(class_num):
    scores = list(map(int, input().split()))
    n = scores[0] 
    scores = scores[1:]
    scores.sort()
    gap = 0
    for i in range(n-1):
        if gap < scores[i+1] - scores[i]:
            gap = scores[i+1] - scores[i]
    result.append([max(scores), min(scores), gap])

for i in range(class_num):
    print("Class {}\nMax {}, Min {}, Largest gap {}".format(
       i + 1, result[i][0], result[i][1], result[i][2]))


    