#최대공약수 최소공배수
from math import gcd

a, b = map(int, input().split())

print(gcd(a, b))
print(a*b//gcd(a, b))