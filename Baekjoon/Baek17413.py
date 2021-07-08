#단어 뒤집기 2 

import sys

word = list(sys.stdin.readline().rstrip())

i = 0
check = 0

while i < len(word):
    if word[i] == "<" :
        i += 1
        while word[i] != ">" :
            i += 1
        i += 1
        
    elif word[i].isalnum():
        check = i
        while i < len(word) and word[i].isalnum():
            i += 1
        temp = word[check:i]
        temp.reverse()
        word[check:i] = temp
        
    else:
        i += 1

print("".join(word))            

# S = input()
# tmp = ''
# ans = ''
# isTag = False
 
# for i in S:
#     if i == ' ':
#         ans += tmp[::-1] + i
#         tmp = ''
#     elif i == '<':
#         isTag = True
#         ans += tmp[::-1] + i
#         tmp = ''
#     elif i == '>':
#         isTag = False
#         ans += i
#     elif isTag:
#          ans += i
#     else:
#         tmp += i
 
# ans += tmp[::-1]
 
# print(ans)
