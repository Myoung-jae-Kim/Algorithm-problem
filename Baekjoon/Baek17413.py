#단어 뒤집기 2 

S = input()
tmp = ''
ans = ''
isTag = False
 
for i in S:
    if i == ' ':
        ans += tmp[::-1] + i
        tmp = ''
    elif i == '<':
        isTag = True
        ans += tmp[::-1] + i
        tmp = ''
    elif i == '>':
        isTag = False
        ans += i
    elif isTag:
         ans += i
    else:
        tmp += i
 
ans += tmp[::-1]
 
print(ans)
