#ROT 13

import sys

line= list(sys.stdin.readline().rstrip())

for i in range(len(line)):

    # 대문자
    if line[i].isupper():
        if ord(line[i])+13 <= 90:
            line[i] = chr(ord(line[i])+13)
        else:
            line[i] = chr(ord(line[i])-13)

    # 소문자
    elif line[i].islower():
        if ord(line[i])+13 <= 122:
            line[i] = chr(ord(line[i])+13)
        else:
            line[i] = chr(ord(line[i])-13)

for each in line:
    print(each, end="")