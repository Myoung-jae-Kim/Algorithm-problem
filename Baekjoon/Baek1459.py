import sys

X, Y, W, S = map(int, sys.stdin.readline().split())
X, Y = min(X, Y), max(X, Y)
m = (X+Y)%2
print(min((X+Y)*W, X*S + (Y-X)*W, (Y-m)*S + m*W))