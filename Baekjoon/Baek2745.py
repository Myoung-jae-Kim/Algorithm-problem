import sys 

before, base = sys.stdin.readline().split() 
base = int(base)
cnt, res = 0, 0 

for c in before[::-1]: 
    target = int(c) if c.isdigit() else ord(c) - 55 
    res += (target * (base**cnt))
    cnt += 1 
    
sys.stdout.write(str(res))
