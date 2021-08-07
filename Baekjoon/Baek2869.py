#달팽이는 올라가고 싶다
import sys

A,B,V = map(int, sys.stdin.readline().split())
Day = int((V-A)/(A-B))

if ((V-A)%(A-B) == 0):
    print(Day + 1)
else:
    print(Day + 2)

