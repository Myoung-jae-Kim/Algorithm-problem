#단어 정렬

N = int(input())
words = []
result = []
for i in range(N):
    words.append(input())

words = list(set(words))
words.sort(key=lambda x : (len(x),x))

print("\n".join(words))