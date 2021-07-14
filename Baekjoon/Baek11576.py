import sys

A, B = map(int, sys.stdin.readline().split())
m = sys.stdin.readline()
before =  list(map(int, sys.stdin.readline().split()))

total = 0
power = 0

for b in before[::-1]:
    total += (b*(A**power))
    power += 1

after = []

while total:
    after.append(str(total % B))
    total //= B

sys.stdout.write(''.join(after[::-1]))