#알파벳 개수

import sys

word = list(sys.stdin.readline().strip())
result = [0] * 26 # a - z 개수

for i in word:
    if i == 'a':
        result[0] += 1
        
    if i == 'b':
        result[1] += 1
        
    if i == 'c':
        result[2] += 1
        
    if i == 'd':
        result[3] += 1
        
    if i == 'e':
        result[4] += 1
        
    if i == 'f':
        result[5] += 1
        
    if i == 'g':
        result[6] += 1
        
    if i == 'h':
        result[7] += 1
        
    if i == 'i':
        result[8] += 1
        
    if i == 'j':
        result[9] += 1
        
    if i == 'k':
        result[10] += 1
        
    if i == 'l':
        result[11] += 1
        
    if i == 'm':
        result[12] += 1
    
    if i == 'n':
        result[13] += 1
        
    if i == 'o':
        result[14] += 1
        
    if i == 'p':
        result[15] += 1
        
    if i == 'q':
        result[16] += 1
        
    if i == 'r':
        result[17] += 1
        
    if i == 's':
        result[18] += 1
        
    if i == 't':
        result[19] += 1
        
    if i == 'u':
        result[20] += 1

    if i == 'v':
        result[21] += 1

    if i == 'w':
        result[22] += 1

    if i == 'x':
        result[23] += 1

    if i == 'y':
        result[24] += 1

    if i == 'z':
        result[25] += 1



for j in result:
    print(j, end = " ")
        