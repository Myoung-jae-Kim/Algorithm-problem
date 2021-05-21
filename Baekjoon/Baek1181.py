#단어 정렬

N = int(input())
words = []
result = []
for i in range(N):
        words.append(list(input()))

words.sort(key=lambda x:(len(x),x))

for i in words:
    if i not in result:
        print(''.join(i))
        result.append(i)