import sys

E, S, M = map(int, sys.stdin.readline().split()) #지구,태양,달
year = 1 #연도


while (True):
    if ((year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0):
        print(year)
        break
    year += 1

