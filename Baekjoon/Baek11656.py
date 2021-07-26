#접미사 배열
from sys import stdin

#\n 제거
S = stdin.readline().rstrip()

#문자열 S에 대한 접미사 리스트
suffixes = []

for i in range(len(S)):
    suffixes.append(S[i:])

suffixes.sort()

for j in suffixes:
    print(j)