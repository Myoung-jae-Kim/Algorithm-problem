#문자열 분석
import sys

while True:
    line = sys.stdin.readline().rstrip('\n') 
    low, up, num, space = 0, 0, 0, 0 
    
    if not line: 
        break 
    
    for l in line: 
        if l.islower(): 
            low += 1
            
        if l.isupper(): 
            up += 1
            
        if l.isdigit(): 
            num += 1 
            
        if l.isspace(): 
            space += 1 
            
    print("{} {} {} {}".format(low, up, num, space))

